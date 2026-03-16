import rclpy
from rclpy.node import Node
from my_robot_interfaces.srv import MoveRobot


class MoveRobotClient(Node):

    def __init__(self):
        super().__init__('move_robot_client')

        self.cli = self.create_client(
            MoveRobot,
            'move_robot'
        )

        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available')

        req = MoveRobot.Request()
        req.distance = 2.0
        req.angle = 90.0

        self.future = self.cli.call_async(req)


def main():
    rclpy.init()
    node = MoveRobotClient()
    rclpy.spin_until_future_complete(node, node.future)

    print(node.future.result())

    rclpy.shutdown()


if __name__ == '__main__':
    main()
    