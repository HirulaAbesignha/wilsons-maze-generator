import pygame
from maze import Maze, Direction
from config import Colors, CELL_SIZE, WALL_THICKNESS


class Renderer:
    
    def __init__(self, maze: Maze, cell_size: int):
        self.maze = maze
        self.cell_size = cell_size
        self.wall_thickness = WALL_THICKNESS
        
        # Calculate window size
        self.width = maze.width * cell_size + WALL_THICKNESS
        self.height = maze.height * cell_size + WALL_THICKNESS + 40
        
        # Initialize Pygame
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Wilson's Algorithm Maze Generator")
        self.font = pygame.font.Font(None, 24)
        self.clock = pygame.time.Clock()
    
    def render(self) -> None:
        #Render the complete maze state
        self.screen.fill(Colors.BACKGROUND)
        
        # Render cells
        for row in self.maze.grid:
            for cell in row:
                self._render_cell(cell)
        
        # Render current walk path
        self._render_walk_path()
        
        # Render walls
        for row in self.maze.grid:
            for cell in row:
                self._render_walls(cell)
        
        # Render status text
        self._render_status()
        
        pygame.display.flip()
    
    def _render_cell(self, cell) -> None:
        #Render a single cell's background
        x = cell.x * self.cell_size + self.wall_thickness
        y = cell.y * self.cell_size + self.wall_thickness
        size = self.cell_size - self.wall_thickness
        
        # Determine color
        if (cell.x, cell.y) in self.maze.walk_set:
            color = Colors.WALK_PATH
        elif cell.visited:
            color = Colors.VISITED
        else:
            color = Colors.UNVISITED
        
        pygame.draw.rect(self.screen, color, (x, y, size, size))
    
    def _render_walk_path(self) -> None:
        #Render the current random walk path as a line
        if len(self.maze.current_walk) < 2:
            return
        
        points = []
        for x, y in self.maze.current_walk:
            center_x = x * self.cell_size + self.cell_size // 2
            center_y = y * self.cell_size + self.cell_size // 2
            points.append((center_x, center_y))
        
        if len(points) >= 2:
            pygame.draw.lines(self.screen, Colors.CURRENT_CELL, False, points, 3)
    
    def _render_walls(self, cell) -> None:
        #Render walls for a single cell
        x = cell.x * self.cell_size
        y = cell.y * self.cell_size
        size = self.cell_size
        thick = self.wall_thickness
        
        # Top wall
        if cell.has_wall(Direction.NORTH):
            pygame.draw.rect(self.screen, Colors.WALL, (x, y, size + thick, thick))
        
        # Right wall
        if cell.has_wall(Direction.EAST):
            pygame.draw.rect(self.screen, Colors.WALL, (x + size, y, thick, size + thick))
        
        # Bottom wall
        if cell.has_wall(Direction.SOUTH):
            pygame.draw.rect(self.screen, Colors.WALL, (x, y + size, size + thick, thick))
        
        # Left wall
        if cell.has_wall(Direction.WEST):
            pygame.draw.rect(self.screen, Colors.WALL, (x, y, thick, size + thick))
    
    def _render_status(self) -> None:
        #Render status text at the bottom
        text_y = self.maze.height * self.cell_size + 10
        
        # Background
        pygame.draw.rect(self.screen, Colors.TEXT_BG, 
                        (0, text_y - 5, self.width, 40))
        
        # Status text
        text_surface = self.font.render(self.maze.status_text, True, Colors.TEXT)
        text_rect = text_surface.get_rect(center=(self.width // 2, text_y + 10))
        self.screen.blit(text_surface, text_rect)
        
        # Instructions
        if self.maze.algorithm_complete:
            inst_text = "Press 'R' to regenerate | ESC to quit"
            inst_surface = self.font.render(inst_text, True, Colors.TEXT)
            inst_rect = inst_surface.get_rect(center=(self.width // 2, text_y + 25))
            self.screen.blit(inst_surface, inst_rect)