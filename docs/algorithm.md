# Wilson's Algorithm: A Deep Dive

> A comprehensive guide to understanding Wilson's Loop-Erased Random Walk algorithm for uniform spanning tree generation.

---

## Table of Contents

- [Introduction](#introduction)
- [What is a Perfect Maze?](#what-is-a-perfect-maze)
- [Algorithm Overview](#algorithm-overview)
- [Step-by-Step Process](#step-by-step-process)
- [Loop-Erased Random Walk](#loop-erased-random-walk)
- [Why Wilson's Algorithm?](#why-wilsons-algorithm)
- [Mathematical Properties](#mathematical-properties)
- [Complexity Analysis](#complexity-analysis)
- [Visual Examples](#visual-examples)
- [Comparison with Other Algorithms](#comparison-with-other-algorithms)
- [Implementation Considerations](#implementation-considerations)
- [References](#references)

---

## Introduction

**Wilson's Algorithm** is a maze generation algorithm invented by computer scientist **David Bruce Wilson** in 1996. It generates **uniform spanning trees**, which in the context of mazes means every possible perfect maze has an equal probability of being generated.

### Key Characteristics

- **Type**: Uniform spanning tree algorithm
- **Bias**: Unbiased (all mazes equally likely)
- **Completeness**: Generates perfect mazes
- **Method**: Loop-erased random walks
- **Discovery**: David Bruce Wilson (1996)

---

## What is a Perfect Maze?

A **perfect maze** (also called a "simply connected maze") has these properties:

### 1. **Exactly One Path**
Between any two cells in the maze, there exists exactly one path. No more, no less.

```
┌─────────┬─────┐
│         │     │
│   ┌─────┘   ┌─┘
│   │         │
└───┴─────────┘
    ↑ Only ONE path from any cell to any other
```

### 2. **No Loops**
The maze contains no circular paths. You cannot start at a cell and return to it without backtracking.

### 3. **Fully Connected**
Every cell is accessible from every other cell. No isolated regions exist.

### 4. **Spanning Tree**
Mathematically, a perfect maze is a **spanning tree** of the grid graph:
- **Spanning**: Includes all vertices (cells)
- **Tree**: Connected graph with no cycles

---

## Algorithm Overview

Wilson's Algorithm builds a maze by performing **loop-erased random walks** from unvisited cells until they connect to the growing maze.

### High-Level Pseudocode

```
1. Choose a random cell and mark it as "visited" (this is the maze seed)

2. While there are unvisited cells:
   a. Choose a random unvisited cell
   b. Perform a random walk from this cell:
      - Move to a random neighbor
      - If you create a loop, erase it
      - Continue until you hit a visited cell
   c. Carve the entire loop-erased path into the maze
   d. Mark all cells in the path as visited

3. Maze complete!
```

---

## Step-by-Step Process

Let's walk through a small 4×4 example:

### Step 1: Initialize

```
┌───┬───┬───┬───┐
│   │   │   │   │
├───┼───┼───┼───┤
│   │ ✓ │   │   │  ← Random cell marked as visited
├───┼───┼───┼───┤
│   │   │   │   │
├───┼───┼───┼───┤
│   │   │   │   │
└───┴───┴───┴───┘
```

### Step 2: Start Random Walk

Pick random unvisited cell (0,0) and start walking:

```
┌───┬───┬───┬───┐
│ 1→│ 2 │   │   │  Walk: (0,0) → (1,0) → (1,1)
├───┼─┴─┼───┼───┤
│   │ ✓ │   │   │  Hit visited cell!
├───┼───┼───┼───┤
│   │   │   │   │
├───┼───┼───┼───┤
│   │   │   │   │
└───┴───┴───┴───┘
```

### Step 3: Carve Path

Carve the walk path into the maze:

```
┌───┬───┬───┬───┐
│ ✓ │ ✓ │   │   │
├───┴───┼───┼───┤
│   ✓   │   │   │
├───┬───┼───┼───┤
│   │   │   │   │
├───┼───┼───┼───┤
│   │   │   │   │
└───┴───┴───┴───┘
```

### Step 4: Loop Erasure Example

Start new walk from (3,0):

```
Step 1: (3,0) → (2,0)
Step 2: (2,0) → (2,1) 
Step 3: (2,1) → (3,1)
Step 4: (3,1) → (3,0)  ← Loop detected!

Path before: [(3,0), (2,0), (2,1), (3,1), (3,0)]
Path after:  [(3,0)]  ← Everything erased back to (3,0)
```

Continue walking from (3,0) again...

---

## Loop-Erased Random Walk

The **loop-erased random walk** (LERW) is the heart of Wilson's Algorithm.

### What is Loop Erasure?

When the random walk visits a cell it has already visited during the current walk, we **erase the loop** by removing all steps between the two visits.

### Visual Example

```
Walk Path:  A → B → C → D → B → E

              D
              ↑
    A → B → C
        ↓
        B → E

Loop detected at B!

After erasure:  A → B → E

    A → B → E
```

### Why Erase Loops?

1. **Perfect Maze Property**: Loops would create cycles, violating the tree property
2. **Uniform Distribution**: Loop erasure ensures unbiased generation
3. **Efficiency**: Prevents infinite walks

### Implementation Details

```python
def erase_loop(walk, cell):
    """
    Erase loop when revisiting a cell in the walk.
    
    Args:
        walk: List of cells in current walk path
        cell: Cell being revisited
    
    Returns:
        Modified walk with loop removed
    """
    # Find first occurrence of cell in walk
    loop_start = walk.index(cell)
    
    # Keep everything up to and including loop_start
    # Discard everything after
    return walk[:loop_start + 1]
```

---

## Why Wilson's Algorithm?

### Advantages

#### 1. **Uniform Distribution**
Every possible spanning tree has equal probability:
```
P(any specific maze) = 1 / (total number of spanning trees)
```

#### 2. **Unbiased**
Unlike many algorithms, Wilson's has no directional bias:
- **Recursive Backtracker**: Tends toward long corridors
- **Prim's**: Slightly biased toward dense branching
- **Wilson's**: Perfectly random

#### 3. **Provably Correct**
Mathematical proof guarantees uniform distribution (Propp-Wilson, 1998).

#### 4. **Beautiful Patterns**
The generation process creates mesmerizing visual patterns.

### Disadvantages

#### 1. **Slow Start**
Early random walks can take a long time to hit the small visited region.

```
Early:  Large unvisited area → Long walks
Later:  Large visited area → Quick walks
```

#### 2. **Memory Usage**
Must track the entire walk path for loop erasure.

#### 3. **Implementation Complexity**
More complex than simpler algorithms like recursive backtracking.

---

## Mathematical Properties

### Uniform Spanning Tree

For a graph G with V vertices, the number of spanning trees is given by **Kirchhoff's Matrix-Tree Theorem**:

```
τ(G) = det(L_reduced)
```

Where L is the Laplacian matrix.

Wilson's Algorithm generates each spanning tree with probability:

```
P(T) = 1 / τ(G)
```

### Loop-Erased Random Walk Properties

The LERW has several interesting properties:

1. **Self-Avoiding**: The final path never revisits cells
2. **Conformal Invariance**: In the limit, LERWs are conformally invariant
3. **Fractal Dimension**: In 2D, the fractal dimension is approximately 1.25

---

## ⏱Complexity Analysis

### Time Complexity

- **Best Case**: O(n) where n is the number of cells
  - Occurs when walks immediately hit the maze
  
- **Average Case**: O(n log n)
  - Expected time for random walks to hit growing maze

- **Worst Case**: O(n²) or worse
  - Theoretical worst case when walks repeatedly form long loops

### Space Complexity

- **O(n)** for the maze grid
- **O(n)** worst case for storing walk paths
- **Total**: O(n)

### Practical Performance

For an n×n grid:

| Size | Cells | Typical Time |
|------|-------|--------------|
| 10×10 | 100 | < 1 second |
| 25×25 | 625 | 1-3 seconds |
| 50×50 | 2,500 | 5-15 seconds |
| 100×100 | 10,000 | 30-90 seconds |

*Performance improves significantly as the algorithm progresses.*

---

## Visual Examples

### Early Stage
```
Visited: ░░░
Unvisited: ▓▓▓▓▓▓▓▓▓▓▓▓▓▓
Walk: ∼∼∼∼∼∼∼∼∼ (long random walks)
```

### Middle Stage
```
Visited: ░░░░░░░░░░
Unvisited: ▓▓▓▓▓▓
Walk: ∼∼∼ (shorter walks)
```

### Late Stage
```
Visited: ░░░░░░░░░░░░░░
Unvisited: ▓▓
Walk: ∼ (very short walks)
```

### Complete Maze
```
┌─────┬───────┬─┐
│     │       │ │
│ ┌─┐ │ ┌───┐ │ │
│ │ │   │   │   │
│ │ └─┬─┘ ┌─┴─┬─┤
│ │   │   │   │ │
│ └───┴───┴───┘ │
│               │
└───────────────┘
```

---

## Comparison with Other Algorithms

| Algorithm | Bias | Speed | Memory | Complexity |
|-----------|------|-------|--------|------------|
| **Wilson's** | None | Medium | Medium | High |
| Recursive Backtracker | Long corridors | Fast | Low | Low |
| Prim's | Dense | Fast | Medium | Medium |
| Kruskal's | None | Fast | High | Medium |
| Eller's | Horizontal | Very Fast | Very Low | Medium |
| Aldous-Broder | None | Slow | Low | Low |

### When to Use Wilson's

**Use Wilson's when:**
- You need perfectly unbiased mazes
- Visual aesthetics matter
- Maze size is reasonable (< 100×100)
- Mathematical correctness is important

**Consider alternatives when:**
- Speed is critical
- Generating very large mazes (> 200×200)
- Memory is constrained
- Simple implementation needed

---

## Implementation Considerations

### 1. **Loop Detection**

Use a set for O(1) loop detection:

```python
walk_set = set(walk_path)

if next_cell in walk_set:
    # Loop detected!
    erase_loop(next_cell)
```

### 2. **Path Storage**

Store paths as lists for efficient erasure:

```python
walk_path = []  # List allows easy slicing
walk_set = set()  # Set allows fast lookup
```

### 3. **Random Selection**

Use efficient random selection:

```python
# Good: O(1) random choice
neighbors = get_neighbors(current)
next_cell = random.choice(neighbors)

# Bad: O(n) filtering
unvisited = [c for c in all_cells if not c.visited]
next_cell = random.choice(unvisited)
```

### 4. **Visited Tracking**

Mark cells visited efficiently:

```python
# Cell-based
cell.visited = True

# Set-based (faster lookup)
visited_set.add((x, y))
```

---

## References

### Academic Papers

1. **Wilson, D. B.** (1996). "Generating random spanning trees more quickly than the cover time". *Proceedings of the 28th ACM Symposium on Theory of Computing*, pp. 296-303.

2. **Propp, J. G., & Wilson, D. B.** (1998). "How to get a perfectly random sample from a generic Markov chain and generate a random spanning tree of a directed graph". *Journal of Algorithms*, 27(2), 170-217.

3. **Lawler, G. F., Schramm, O., & Werner, W.** (2004). "Conformal invariance of planar loop-erased random walks and uniform spanning trees". *Annals of Probability*, 32(1B), 939-995.

### Online Resources

- [Wikipedia: Loop-erased random walk](https://en.wikipedia.org/wiki/Loop-erased_random_walk)
- [Wikipedia: Uniform spanning tree](https://en.wikipedia.org/wiki/Uniform_spanning_tree)
- [Jamis Buck's Maze Generation Algorithms](https://weblog.jamisbuck.org/2011/1/20/maze-generation-wilson-s-algorithm)
- [Think Labyrinth: Maze Algorithms](http://www.astrolog.org/labyrnth/algrithm.htm)

### Books

- **Mazes for Programmers** by Jamis Buck (2015)
  - Comprehensive coverage of maze algorithms including Wilson's

- **The Algorithm Design Manual** by Steven Skiena (2008)
  - Graph algorithms and spanning trees

---

## Further Reading

### Related Algorithms

- **Aldous-Broder Algorithm**: Another uniform spanning tree algorithm
- **Random Walk Algorithms**: Foundation of Wilson's algorithm
- **Markov Chain Monte Carlo**: Theoretical framework

### Applications Beyond Mazes

- **Network Design**: Creating redundancy-free networks
- **Game Level Generation**: Procedural dungeon generation
- **Art**: Generative art using uniform spanning trees
- **Physics**: Statistical mechanics models

---

<p align="center">
  <strong>Understanding Wilson's Algorithm opens doors to elegant procedural generation techniques.</strong>
</p>

<p align="center">
  <a href="../README.md">← Back to Main README</a> | 
  <a href="usage.md">Usage Guide →</a>
</p>

---

<p align="center">
  <em>Last updated: December 2025</em>
</p>