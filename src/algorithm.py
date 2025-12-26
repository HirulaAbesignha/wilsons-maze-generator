from typing import Optional, Tuple
import random
from maze import Maze


class WilsonAlgorithm:
    def __init__(self, maze: Maze):
        self.maze = maze
        self.state = "init"
        self.current_pos: Optional[Tuple[int, int]] = None
        
    def initialize(self) -> None:
        #Mark one random cell as visited
        x = random.randint(0, self.maze.width - 1)
        y = random.randint(0, self.maze.height - 1)
        cell = self.maze.get_cell(x, y)
        if cell:
            cell.visited = True
        self.state = "select_start"
        self.maze.status_text = "Initial cell marked"
    
    def step(self) -> bool:
        #Execute one step of the algorithm. Returns True if complete
        
        if self.state == "init":
            self.initialize()
            return False
        
        if self.state == "select_start":
            # Select a new random unvisited cell to start walk
            pos = self.maze.get_random_unvisited()
            if pos is None:
                self.maze.algorithm_complete = True
                self.maze.status_text = "Maze Complete!"
                return True
            
            self.current_pos = pos
            self.maze.current_walk = [pos]
            self.maze.walk_set = {pos}
            self.state = "random_walk"
            self.maze.status_text = f"Starting walk from {pos}"
            return False
        
        if self.state == "random_walk":
            # Perform one step of random walk
            if self.current_pos is None:
                self.state = "select_start"
                return False
            
            x, y = self.current_pos
            neighbors = self.maze.get_neighbors(x, y)
            
            if not neighbors:
                self.state = "select_start"
                return False
            
            # Choose random neighbor
            _, nx, ny = random.choice(neighbors)
            
            # Check if we hit a visited cell
            next_cell = self.maze.get_cell(nx, ny)
            if next_cell and next_cell.visited:
                # Walk complete - carve the path
                self.maze.current_walk.append((nx, ny))
                self.carve_path()
                self.state = "select_start"
                return False
            
            # Check for loop
            if (nx, ny) in self.maze.walk_set:
                # Erase loop
                self.erase_loop(nx, ny)
                self.maze.status_text = f"Loop erased at ({nx}, {ny})"
            else:
                # Continue walk
                self.maze.current_walk.append((nx, ny))
                self.maze.walk_set.add((nx, ny))
            
            self.current_pos = (nx, ny)
            unvisited = self.maze.count_unvisited()
            self.maze.status_text = f"Walking... ({unvisited} cells remaining)"
            return False
        
        return False
    
    def erase_loop(self, loop_x: int, loop_y: int) -> None:
        #Remove loop from walk path when revisiting a cell in the walk
        # Find where the loop starts
        loop_index = None
        for i, (x, y) in enumerate(self.maze.current_walk):
            if x == loop_x and y == loop_y:
                loop_index = i
                break
        
        if loop_index is not None:
            # Erase everything after loop_index
            self.maze.current_walk = self.maze.current_walk[:loop_index + 1]
            
            # Update walk set
            self.maze.walk_set = set(self.maze.current_walk)
    
    def carve_path(self) -> None:
        #Carve the entire walk path into the maze
        for i in range(len(self.maze.current_walk) - 1):
            x1, y1 = self.maze.current_walk[i]
            x2, y2 = self.maze.current_walk[i + 1]
            
            # Carve passage
            self.maze.carve_passage(x1, y1, x2, y2)
            
            # Mark as visited
            cell = self.maze.get_cell(x1, y1)
            if cell:
                cell.visited = True
        
        # Clear walk state
        self.maze.current_walk = []
        self.maze.walk_set = set()