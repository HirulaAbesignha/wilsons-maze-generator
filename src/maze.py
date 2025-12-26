from enum import Enum
from typing import List, Optional, Set, Tuple
from dataclasses import dataclass
import random


class Direction(Enum):
    #Cardinal directions for maze navigation
    NORTH = (0, -1)
    EAST = (1, 0)
    SOUTH = (0, 1)
    WEST = (-1, 0)
    
    def opposite(self) -> 'Direction':
        #Returns the opposite direction
        opposites = {
            Direction.NORTH: Direction.SOUTH,
            Direction.SOUTH: Direction.NORTH,
            Direction.EAST: Direction.WEST,
            Direction.WEST: Direction.EAST
        }
        return opposites[self]


@dataclass
class Cell:
    #Represents a single cell in the maze grid
    x: int
    y: int
    walls: dict
    visited: bool = False
    
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.walls = {
            Direction.NORTH: True,
            Direction.EAST: True,
            Direction.SOUTH: True,
            Direction.WEST: True
        }
        self.visited = False
    
    def remove_wall(self, direction: Direction) -> None:
        #Remove wall in the specified direction
        self.walls[direction] = False
    
    def has_wall(self, direction: Direction) -> bool:
        #Check if wall exists in the specified direction
        return self.walls[direction]


class Maze:
    #Core maze data structure
    
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.grid: List[List[Cell]] = []
        self._initialize_grid()
        
        # Algorithm state
        self.current_walk: List[Tuple[int, int]] = []
        self.walk_set: Set[Tuple[int, int]] = set()
        self.algorithm_complete = False
        self.status_text = "Initializing..."
        
    def _initialize_grid(self) -> None:
        #Create the 2D grid of cells
        self.grid = [[Cell(x, y) for x in range(self.width)] 
                     for y in range(self.height)]
    
    def get_cell(self, x: int, y: int) -> Optional[Cell]:
        #Safely retrieve a cell from the grid
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.grid[y][x]
        return None
    
    def get_neighbors(self, x: int, y: int) -> List[Tuple[Direction, int, int]]:
        #Get valid neighboring cells with their directions
        neighbors = []
        for direction in Direction:
            dx, dy = direction.value
            nx, ny = x + dx, y + dy
            if self.get_cell(nx, ny) is not None:
                neighbors.append((direction, nx, ny))
        return neighbors
    
    def carve_passage(self, x1: int, y1: int, x2: int, y2: int) -> None:
        #Remove walls between two adjacent cells
        cell1 = self.get_cell(x1, y1)
        cell2 = self.get_cell(x2, y2)
        
        if cell1 is None or cell2 is None:
            return
        
        # Determine direction
        dx, dy = x2 - x1, y2 - y1
        
        if dx == 1:  # Moving East
            cell1.remove_wall(Direction.EAST)
            cell2.remove_wall(Direction.WEST)
        elif dx == -1:  # Moving West
            cell1.remove_wall(Direction.WEST)
            cell2.remove_wall(Direction.EAST)
        elif dy == 1:  # Moving South
            cell1.remove_wall(Direction.SOUTH)
            cell2.remove_wall(Direction.NORTH)
        elif dy == -1:  # Moving North
            cell1.remove_wall(Direction.NORTH)
            cell2.remove_wall(Direction.SOUTH)
    
    def count_unvisited(self) -> int:
        #Count remaining unvisited cells
        count = 0
        for row in self.grid:
            for cell in row:
                if not cell.visited:
                    count += 1
        return count
    
    def get_random_unvisited(self) -> Optional[Tuple[int, int]]:
        #Select a random unvisited cell
        unvisited = [(cell.x, cell.y) for row in self.grid 
                     for cell in row if not cell.visited]
        return random.choice(unvisited) if unvisited else None
