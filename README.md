# ROS2 Communication Study

ROS2 Python(`rclpy`)을 사용하여 **ROS 통신 방식 3가지**를 구현한 실습 프로젝트입니다.

이 프로젝트는 ROS2의 기본 개념인 **Node, Topic, Service, Action** 구조를 이해하기 위해 작성되었습니다.

---

# Project Structure

```
ros2-study
├── README.md
└── src
    ├── my_py_pkg
    │   ├── package.xml
    │   ├── setup.py
    │   ├── setup.cfg
    │   ├── resource
    │   ├── test
    │   └── my_py_pkg
    │       ├── __init__.py
    │       ├── my_node.py
    │       ├── publisher_node.py
    │       ├── subscriber_node.py
    │       ├── robot_pose_publisher.py
    │       ├── robot_pose_subscriber.py
    │       ├── move_robot_server.py
    │       ├── move_robot_client.py
    │       └── move_distance_server.py
    │
    └── my_robot_interfaces
```
---

# ROS Communication Types

ROS에서는 노드 간 데이터 통신을 위해 **3가지 방식**을 사용합니다.

| Type    | Description | Example |
| ------- | ----------- | ------- |
| Topic   | 비동기 메시지 통신  | 센서 데이터  |
| Service | 요청 / 응답 통신  | 명령 처리   |
| Action  | 장시간 작업 처리   | 로봇 이동   |

---

# 1. Topic Example

Publisher가 메시지를 발행하고 Subscriber가 메시지를 구독합니다.

### Publisher

```
publisher_node.py
```

### Subscriber

```
subscriber_node.py
```

### 실행

터미널1

```
ros2 run my_py_pkg publisher_node
```

터미널2

```
ros2 run my_py_pkg subscriber_node
```

---

# 2. Service Example

Service는 **Request / Response 방식 통신**입니다.

### Server

```
move_robot_server.py
```

### Client

```
move_robot_client.py
```

### 실행

터미널1

```
ros2 run my_py_pkg move_robot_server
```

터미널2

```
ros2 run my_py_pkg move_robot_client
```

---

# 3. Action Example

Action은 **시간이 오래 걸리는 작업을 처리하기 위한 통신 방식**입니다.

Action은 다음 3가지 메시지를 사용합니다.

* Goal
* Feedback
* Result

### Action Server

```
move_distance_server.py
```

### Goal 보내기

```
ros2 action send_goal /move_distance my_robot_interfaces/action/MoveDistance "{distance: 5.0}"
```

---

# Build

워크스페이스 루트에서 실행

```
cd ros2_ws
colcon build
```

환경 설정

```
source install/setup.bash
```

---

# Technologies

* ROS2 Humble
* Python
* rclpy
* Ubuntu

---

# Author

Hyeongjune Kim
ROS2 Study Project
