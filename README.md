# RP_Cristino_Garcia_Sanchez_25
# Flappy Bird – Python Game (GAME Branch)

This branch contains the **stand-alone Python/Pygame implementation** of the Flappy Bird game.  
It represents the base version of the project *before* integrating ROS nodes, services, parameters, and multi-process communication.

This branch does **NOT require ROS**.  
It can be executed as a standard Python game.

---

## 🎮 Overview

The GAME version includes:

- Bird physics (jump, gravity, velocity cap)
- Procedural pipe generation
- Dynamic difficulty (gap size decreases)
- Collision detection with pipes and boundaries
- Lives system and temporary invincibility
- Welcome screen, Play screen, and Game Over screen
- Custom rendering of the bird, pipes, and background

This branch serves as the foundation for the ROS implementation in the `ROS` branch.

---

## 📁 Project Structure
```md
GAME/
├── game.py ← Main Python/Pygame implementation of Flappy Bird
└── README.md ← This documentation file
```

---

## Requirements
- **Python 3**
- **Pygame**

Install Pygame:

```bash
pip install pygame
```
## How to Run the Game
Run the Python file directly:

```bash
python3 game.py
```

A graphical window will open with the full Flappy Bird game.

---

## Controls

| Key          | Action                    |
|--------------|---------------------------|
| **SPACE**    | Jump / flap               |
| **Mouse Click** | Jump                  |
| **R**        | Restart after Game Over   |
| **Close Window** | Quit game            |


## Authors

- **Ana Cristino Prieto**
- **Andrea García Ruiz**
- **Paula Sánchez Sanz**


