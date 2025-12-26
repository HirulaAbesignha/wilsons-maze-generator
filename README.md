# Wilson's Algorithm Maze Generator

[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Pygame](https://img.shields.io/badge/pygame-2.5+-green.svg)](https://www.pygame.org/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

> A production-quality, real-time visualization of Wilson's Algorithm for perfect maze generation, built with Python and Pygame.

---

## Table of Contents

- [About](#about)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Controls](#controls)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [Documentation](#documentation)
- [License](#license)
- [Acknowledgments](#acknowledgments)

---

## About

This project implements **Wilson's Algorithm**, a sophisticated maze generation technique that creates **perfect mazes**—mazes with exactly one path between any two points and no loops. Unlike simpler algorithms, Wilson's generates mazes through loop-erased random walks, producing elegant patterns and guaranteeing a uniform distribution across all possible maze configurations.

### Why Wilson's Algorithm?

- **Perfect Mazes**: No isolated regions or circular paths
- **Uniform Distribution**: Every possible maze is equally likely
- **Visually Fascinating**: The generation process creates mesmerizing patterns
- **Educational**: Excellent for learning advanced procedural generation

For a detailed explanation of how the algorithm works, see [docs/algorithm.md](docs/algorithm.md).

---

## Features

- **Faithful Algorithm Implementation** - Correct Wilson's Algorithm with guaranteed perfect mazes
- **Real-Time Visualization** - Watch every step of the generation process
- **Loop Erasure Animation** - See loops detected and removed instantly
- **Interactive Controls** - Pause, speed up, regenerate on the fly
- **Clean Architecture** - Modular, documented, production-ready code
- **Educational** - Perfect for understanding maze algorithms
- **Smooth Animation** - 60 FPS rendering with Pygame
- **Highly Configurable** - Customize colors, sizes, and speeds

---

## Installation

### Prerequisites

- **Python 3.8+** ([Download](https://www.python.org/downloads/))
- **pip** (included with Python)

### Clone the Repository

```bash
git clone https://github.com/HirulaAbesignha/wilson-maze-generator.git
cd wilson-maze-generator
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

That's it! You're ready to generate mazes.

---

## Usage

### Basic Usage

Run the main script:

```bash
python src/main.py
```

You'll be prompted to enter maze dimensions:

```
=== Wilson's Algorithm Maze Generator ===
Enter maze width (cells, 5-50): 20
Enter maze height (cells, 5-50): 20
```

### Quick Start Examples

```bash
# Small maze (fast generation)
# Enter: 10x10

# Medium maze (balanced)
# Enter: 25x25

# Large maze (impressive visuals)
# Enter: 40x40
```

### Programmatic Usage

```python
from src.maze import Maze
from src.algorithm import WilsonAlgorithm

# Create maze
maze = Maze(30, 30)
algorithm = WilsonAlgorithm(maze)

# Generate step by step
while not algorithm.step():
    pass

# Maze is ready!
print(f"Generated {maze.width}x{maze.height} maze")
```

---

## Controls

| Key | Action |
|-----|--------|
| <kbd>SPACE</kbd> | Pause/Resume generation |
| <kbd>↑</kbd> | Increase generation speed |
| <kbd>↓</kbd> | Decrease generation speed |
| <kbd>R</kbd> | Regenerate new maze |
| <kbd>ESC</kbd> | Exit application |

### Visual Guide

- 🟦 **Dark Blue** - Unvisited cells
- 🟦 **Light Blue** - Visited cells (completed maze)
- 🟨 **Yellow** - Current random walk path
- 🔴 **Red Line** - Active walk trail
- ⬜ **White** - Maze walls

---

## Configuration

Customize the generator by editing `src/config.py`:

### Window & Rendering

```python
CELL_SIZE = 30           # Size of each cell (pixels)
WALL_THICKNESS = 2       # Wall rendering thickness
FPS = 60                 # Frame rate
```

### Colors

```python
class Colors:
    BACKGROUND = (15, 15, 25)      # Dark background
    WALL = (220, 220, 230)         # White walls
    UNVISITED = (30, 30, 45)       # Dark blue
    VISITED = (45, 55, 85)         # Light blue
    WALK_PATH = (255, 200, 50)     # Yellow
    CURRENT_CELL = (255, 100, 100) # Red
```

### Maze Limits

```python
MIN_MAZE_SIZE = 5        # Minimum dimensions
MAX_MAZE_SIZE = 50       # Maximum dimensions
```

---

## Contributing

Contributions are **welcome and encouraged**! This project is actively maintained and open to improvements.

### How to Contribute

1. **Fork the repository**
   - Click the "Fork" button at the top right of this page

2. **Clone your fork**
   ```bash
   git clone https://github.com/your-username/wilson-maze-generator.git
   cd wilson-maze-generator
   ```

3. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```

4. **Make your changes**
   - Write clean, documented code
   - Follow existing code style (PEP 8)
   - Add tests if applicable

5. **Commit your changes**
   ```bash
   git add .
   git commit -m "Add: Brief description of your feature"
   ```

6. **Push to your fork**
   ```bash
   git push origin feature/amazing-feature
   ```

7. **Open a Pull Request**
   - Go to the original repository
   - Click "New Pull Request"
   - Select your fork and branch
   - Describe your changes in detail

### Contribution Guidelines

- **Code Style**: Follow PEP 8, use type hints
- **Documentation**: Update relevant docs
- **Testing**: Add tests for new features
- **Commits**: Use clear, descriptive commit messages
- **Issues**: Check existing issues before creating new ones

### Good First Issues

Looking for ways to contribute? Check out issues labeled:
- `good first issue` - Perfect for newcomers
- `help wanted` - Community assistance needed
- `enhancement` - New feature proposals

### Development Setup

```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
pytest tests/

# Format code
black src/

# Lint code
flake8 src/
```

---

## Documentation

- **[Algorithm Explanation](docs/algorithm.md)** - Deep dive into Wilson's Algorithm
- **[Usage Guide](docs/usage.md)** - Detailed usage examples
- **[API Reference](docs/api.md)** - Code documentation

---

## Acknowledgments

- **David Bruce Wilson** - Creator of Wilson's Algorithm (1996)
- **[Jamis Buck](https://weblog.jamisbuck.org/)** - Excellent maze algorithm resources
- **Pygame Community** - Outstanding game development library
- **Contributors** - Thank you for making this project better!

---

## Project Stats

![GitHub stars](https://img.shields.io/github/stars/HirulaAbesignha/wilson-maze-generator?style=social)
![GitHub forks](https://img.shields.io/github/forks/HirulaAbesignha/wilson-maze-generator?style=social)
![GitHub issues](https://img.shields.io/github/issues/HirulaAbesignha/wilson-maze-generator)
![GitHub pull requests](https://img.shields.io/github/issues-pr/HirulaAbesignha/wilson-maze-generator)

---

## Contact & Support

- **Issues**: [GitHub Issues](https://github.com/HirulaAbesignha/wilson-maze-generator/issues)
- **Discussions**: [GitHub Discussions](https://github.com/HirulaAbesignha/wilson-maze-generator/discussions)
- **Email**: hirulapinibinda01
---

<p align="center">
  <strong>If you find this project useful, please consider giving it a star!</strong>
</p>

<p align="center">
  Made with Python | <a href="#-wilsons-algorithm-maze-generator">Back to Top ↑</a>
</p>