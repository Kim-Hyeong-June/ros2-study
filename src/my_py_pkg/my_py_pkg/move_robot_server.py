import rclpy
from rclpy.node import Node

from my_robot_interfaces.srv import MoveRobot


class MoveRobotServer(Node):

    def __init__(self):
        super().__init__('move_robot_server')

        self.srv = self.create_service(
            MoveRobot,
            'move_robot',
            self.move_robot_callback
        )

    def move_robot_callback(self, request, response):

        self.get_logger().info(
            f"Move distance: {request.distance}, angle: {request.angle}"
        )

        # 로봇 동작 처리 (예시)
        response.success = True
        response.message = "Robot moved"

        return response


def main():
    rclpy.init()
    node = MoveRobotServer()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
    