# Flappy Bird – ROS Implementation (ROS Branch)


This branch contains the **ROS version** of the Flappy Bird project.  
It integrates the original Python/Pygame game into a distributed ROS system using:

- Publishers & Subscribers  
- Custom Services  
- Parameters  
- Launch files  
- Multi-node communication  

This branch is the full robotics implementation of the project.

---

##  Dependencies

- **ROS Noetic**
- **Python 3**
- **Pygame**

```bash
  pip install pygame
```
---
## How to run the program

You can run all the nodes at the same time using the launch file or running node by node, both procedures are explained below.

---
## Launch File

Start the whole game with one command

´´´bash
roslaunch rp_Cristino_Garcia_Sanchez_25 flappy_bird_game.launch
´´´

---
## Node by Node Execution
**Terminal 1**

```bash
  roscore
```

**Terminal 2**

```bash
rosrun rp_Cristino_Garcia_Sanchez_25 game_node.py
```

**Terminal 3**

```bash
rosrun rp_Cristino_Garcia_Sanchez_25 info_user.py
```

**Terminal 4**

```bash
rosrun rp_Cristino_Garcia_Sanchez_25 control_node.py
```

**Terminal 5**

```bash
rosrun rp_Cristino_Garcia_Sanchez_25 result_game.py
```

---
## Game Controls

| Key            | Action                    |
|----------------|----------------------------|
| **SPACE**      | Jump / Start / Continue   |
| **R**          | Reset to Phase 1          |
| **Close Window** | Quit game               |


## System Overview

The ROS architecture is composed of 4 nodes, 2 services, 3 parameters, and a launch file.

Below is the full description of each component.

---

## Nodes
### 1 info_user.py

**Type**: Publisher (interactive)

Collects **user information** from keyboard input: Name, Username, Age

Publishes to:

|Topic	| Message |
|-------|---------|
|`/user_information`	| `user_msg` |


### 2 game_node.py

**Type**: Main Game Node (ROS + Pygame)

**Responsibilities**:

- Manages the game phases:

- Phase 1 – Welcome Screen

- Phase 2 – Playing

- Phase 3 – Game Over

- Updates bird physics, collisions, scoring, lives

- Reads keyboard commands (SPACE, R)

- Uses ROS parameters

- Publishes the final score

- Provides ROS services

#### Subscribes to:

| Topic              | Type            |
|--------------------|-----------------|
| `/user_information` | `user_msg`      |
| `/keyboard_control` | `std_msgs/String` |

#### Publishes:

| Topic                | Type             |
|----------------------|------------------|
| `/result_information` | `std_msgs/Int64` |

#### Provides Services:

| Service        | Description                               |
|----------------|-------------------------------------------|
| `/difficulty`  | Change game difficulty (easy/medium/hard) |
| `/user_score`  | Returns user’s score percentage           |

#### Parameters:

| Parameter              | Description                       |
|------------------------|-----------------------------------|
| `/user_name`           | Stores latest username            |
| `/change_player_color` | 1 = Red, 2 = Purple, 3 = Blue     |
| `/screen_param`        | phase1 / phase2 / phase3          |



### 3 control_node.py

**Type**: Keyboard Controller

**Publishes keyboard commands to the game**:
| Key            | Action                    |
|----------------|----------------------------|
| **SPACE**      | Jump / Start / Continue   |
| **R**          | Reset to Phase 1          |

**Publishes to**:

| Topic                | Type             |
|----------------------|------------------|
| `/keyboard_control` | `std_msgs/String` |


### 4 result_game.py

**Type**: Subscriber + Service Client

**Listens to**: user information, final score, Calls /user_score service

**Prints**: Player info, Final score, Percentage (relative to global max score)

**Subscribes to**:

| Topic                | Type             |
|----------------------|------------------|
| `/user_information` | `user_msg` |
|`/result_information` | `std_msgs/Int64` |


**Calls services**:
| Service                | Purpose             |
|----------------------|------------------|
| `/user_score` | `Compute score percentage` |

## Services
### 1 SetGameDifficulty.srv

``` srv
SetGameDifficulty.srv
string level

bool success
```

**Usage**:

```bash
rosservice call /difficulty "level: 'easy'"
```

**IMPORTANT** Works only during Phase 1 (Welcome Screen).

### 2 GetUserScore.srv

```srv
string username

float32 percentage
```

**Usage:**
```bash
rosservice call /user_score "username: 'pepe'"
``` 

**Returns**:

```ini
percentage = (user_best_score / global_best_score) * 100
```

## Parameters

Modify parameters while running the game.

**Bird Colors**

```bash
rosparam set /change_player_color 1   # Red
rosparam set /change_player_color 2   # Purple
rosparam set /change_player_color 3   # Blue
```

**Check User Name**

```bash
rosparam get /user_name
```

**Check phase of the game**

```bash
rosparam get /screen_param
```

---

## Authors
- **Ana Cristino Prieto**
- **Andrea García Ruiz**
- **Paula Sánchez Sanz**
