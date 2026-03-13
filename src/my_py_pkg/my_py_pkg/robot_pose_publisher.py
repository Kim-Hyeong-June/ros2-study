import rclpy
from rclpy.node import Node
from my_robot_interfaces.msg import RobotPose


class RobotPosePublisher(Node):

    def __init__(self):
        super().__init__('robot_pose_publisher')

        self.publisher = self.create_publisher(
            RobotPose,
            'robot_pose',
            10
        )

        self.timer = self.create_timer(1.0, self.publish_pose)

    def publish_pose(self):
        msg = RobotPose()

        msg.x = 1.0
        msg.y = 2.0
        msg.theta = 0.5

        self.publisher.publish(msg)

        self.get_logger().info(
            f'Publishing: x={msg.x}, y={msg.y}, theta={msg.theta}'
        )


def main(args=None):
    rclpy.init(args=args)

    node = RobotPosePublisher()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()
    