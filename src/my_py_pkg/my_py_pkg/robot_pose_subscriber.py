import rclpy
from rclpy.node import Node
from my_robot_interfaces.msg import RobotPose


class RobotPoseSubscriber(Node):

    def __init__(self):
        super().__init__('robot_pose_subscriber')

        self.subscription = self.create_subscription(
            RobotPose,
            'robot_pose',
            self.callback,
            10
        )

    def callback(self, msg):

        self.get_logger().info(
            f'Received: x={msg.x}, y={msg.y}, theta={msg.theta}'
        )


def main(args=None):

    rclpy.init(args=args)

    node = RobotPoseSubscriber()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()
    