import pygame
import sys
from typing import Tuple

from maze import Maze
from algorithm import WilsonAlgorithm
from renderer import Renderer
from config import (
    CELL_SIZE, FPS, MIN_MAZE_SIZE, MAX_MAZE_SIZE,
    DEFAULT_GENERATION_SPEED, MAX_GENERATION_SPEED
)


class MazeApp:

    def __init__(self, width: int, height: int):
        self.maze = Maze(width, height)
        self.algorithm = WilsonAlgorithm(self.maze)
        self.renderer = Renderer(self.maze, CELL_SIZE)
        self.running = True
        self.generation_speed = DEFAULT_GENERATION_SPEED
        self.paused = False
    
    def handle_events(self) -> None:
        #Process user input events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                
                elif event.key == pygame.K_r:
                    # Regenerate maze
                    self.maze = Maze(self.maze.width, self.maze.height)
                    self.algorithm = WilsonAlgorithm(self.maze)
                    self.renderer.maze = self.maze
                
                elif event.key == pygame.K_SPACE:
                    self.paused = not self.paused
                
                elif event.key == pygame.K_UP:
                    self.generation_speed = min(
                        MAX_GENERATION_SPEED, 
                        self.generation_speed + 1
                    )
                
                elif event.key == pygame.K_DOWN:
                    self.generation_speed = max(1, self.generation_speed - 1)
    
    def update(self) -> None:
        #Update algorithm state
        if not self.maze.algorithm_complete and not self.paused:
            for _ in range(self.generation_speed):
                if self.algorithm.step():
                    break
    
    def run(self) -> None:
        #Main game loop
        while self.running:
            self.handle_events()
            self.update()
            self.renderer.render()
            self.renderer.clock.tick(FPS)
        
        pygame.quit()


def get_user_input() -> Tuple[int, int]:
    #Prompt user for maze dimensions with validation
    while True:
        try:
            print("\n=== Wilson's Algorithm Maze Generator ===")
            width = int(input(f"Enter maze width (cells, {MIN_MAZE_SIZE}-{MAX_MAZE_SIZE}): "))
            height = int(input(f"Enter maze height (cells, {MIN_MAZE_SIZE}-{MAX_MAZE_SIZE}): "))
            
            if MIN_MAZE_SIZE <= width <= MAX_MAZE_SIZE and MIN_MAZE_SIZE <= height <= MAX_MAZE_SIZE:
                return width, height
            else:
                print(f"Error: Dimensions must be between {MIN_MAZE_SIZE} and {MAX_MAZE_SIZE}.")
        
        except ValueError:
            print("Error: Please enter valid integers.")
        except KeyboardInterrupt:
            print("\nExiting...")
            sys.exit(0)


def main():
    #Application entry point
    width, height = get_user_input()
    
    print(f"\nGenerating {width}x{height} maze using Wilson's Algorithm...")
    print("\nControls:")
    print("  SPACE - Pause/Resume")
    print("  UP/DOWN - Adjust speed")
    print("  R - Regenerate maze")
    print("  ESC - Quit")
    
    app = MazeApp(width, height)
    app.run()


if __name__ == "__main__":
    main()