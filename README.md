# maze_game

# 2D Maze Game

A simple yet engaging 2D maze game built with Python and Pygame. Navigate through a randomly generated maze to reach the goal!

## 🎮 Game Features

- **Randomly Generated Mazes**: Each game session features a unique maze layout
- **Simple Controls**: Use arrow keys to navigate through the maze
- **Visual Feedback**: Clear visual distinction between walls, paths, player, and goal
- **Win Condition**: Reach the green goal square to win the game

## 🚀 Getting Started

### Prerequisites

Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

### Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/maze-game.git
cd maze-game
```

2. Install the required dependency:
```bash
pip install pygame
```

### Running the Game

Run the game with:
```bash
python maze_game.py
```

## 🎯 How to Play

- **Objective**: Navigate the blue square (player) to the green square (goal)
- **Controls**:
  - ↑ Arrow Key: Move up
  - ↓ Arrow Key: Move down
  - ← Arrow Key: Move left
  - → Arrow Key: Move right
- **Rules**: You can only move through white paths, black areas are walls
- **Winning**: Reach the green goal square in the bottom-right corner

## 🛠️ Technical Details

### Game Specifications
- **Grid Size**: 15x15 cells
- **Cell Size**: 40x40 pixels
- **Window Resolution**: 600x600 pixels
- **Frame Rate**: 60 FPS

### Color Scheme
- **White**: Walkable paths
- **Black**: Walls and boundaries
- **Blue**: Player position
- **Green**: Goal position
- **Red**: Win message text

### Maze Generation
The game uses a recursive backtracking algorithm to generate random mazes, ensuring:
- Every maze is solvable
- Unique layout each time you play
- Proper connectivity between start and end points

## 📁 Project Structure

```
maze-game/
│
├── maze_game.py          # Main game file
└── README.md            # Project documentation
```

## 🔧 Code Overview

The game consists of several key functions:

- `generate_maze()`: Creates a random maze using recursive backtracking
- `draw_maze()`: Renders the maze, player, and goal on screen
- `main()`: Main game loop handling events and game state

## 🎨 Customization Ideas

Want to modify the game? Here are some ideas:

- **Change maze size**: Modify `ROWS` and `COLS` variables
- **Adjust difficulty**: Larger mazes = more challenging
- **New colors**: Update color constants for different themes
- **Add features**: Timer, multiple levels, collectibles, enemies

## 🤝 Contributing

Feel free to fork this project and submit pull requests for any improvements:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🐛 Known Issues

- None currently reported

## 📞 Contact

If you have any questions or suggestions, feel free to reach out or open an issue!

---

**Enjoy navigating through the maze! 🌟**
