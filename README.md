# RP_Cristino_Garcia_Sanchez_25
# FLAPPY BIRD – Robotics Project

This repository contains the final assignment for the Robotics Programming course.  
The project consists of implementing a complete, modular Flappy Bird game using ROS, Python, and Pygame.

All ROS-related work is located in the **ROS** branch of this repository.

---

## 🎮 Project Overview

The objective of this project is to recreate the Flappy Bird game while integrating several robotics concepts:

- Node communication through publishers/subscribers  
- Custom services and parameters  
- Launch files for multi-node execution  
- Real-time control using the keyboard  
- Runtime configuration via ROS parameters  

The game is fully functional and demonstrates how ROS can be used to coordinate parallel processes.

---

## 🧩 Main Features

- Complete Flappy Bird game with graphics (Pygame)
- Multi-node ROS architecture
- Services for difficulty control and score evaluation
- Runtime player configuration (name, username, age)
- Keyboard-based control
- Parameter-based customization (color, phases)
- Automatic launch with `.launch` file

---

## 📁 Repository Structure
main/
 ├── README.md           ← You are here
 

ROS branch:
 ├── game_node.py
 ├── control_node.py
 ├── info_user.py
 ├── result_game.py
 ├── srv/
 ├── msg/
 ├── launch/
 └── README.md           ← Full ROS documentation


