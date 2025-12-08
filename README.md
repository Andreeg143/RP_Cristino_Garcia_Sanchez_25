# RP_Cristino_Garcia_Sanchez_25
# FLAPPY BIRD – Robotics Project

This repository contains the final assignment for the Robotics Programming course.  
The project consists of implementing a complete, modular Flappy Bird game using ROS, Python, and Pygame.

All ROS-related work is located in the **ROS** branch of this repository.

## 📁 Repository Structure

This repository contains three main components:  
the **main branch**, the **ROS branch**, and the **GAME branch**.

```md

main/
 └── README.md                 ← General project description

ROS/
 ├── game_node.py              ← Main ROS + Pygame game logic
 ├── control_node.py           ← Keyboard control (SPACE / R)
 ├── info_user.py              ← User information input (name, username, age)
 ├── result_game.py            ← Final score + percentage display (service client)
 │
 ├── srv/
 │    ├── GetUserScore.srv     ← Returns a player's score percentage
 │    └── SetGameDifficulty.srv← Changes game difficulty (easy/medium/hard)
 │
 ├── msg/
 │    └── user_msg.msg         ← Custom message for sending user info
 │
 ├── launch/
 │    └── flappy_bird_game.launch ← Launches all ROS nodes (xterm windows included)
 │
 └── README.md                 ← Full ROS code documentation
 
GAME/
 ├── game.py                   ← Stand-alone Python/Pygame version of Flappy Bird
 └── README.md                 ← Documentation for the non-ROS version


```
## Authors

- **Ana Cristino Prieto**
- **Andrea García Ruiz**
- **Paula Sánchez Sanz**

