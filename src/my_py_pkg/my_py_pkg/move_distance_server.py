import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer

from my_robot_interfaces.action import MoveDistance


class MoveDistanceServer(Node):

    def __init__(self):
        super().__init__('move_distance_server')

        self._action_server = ActionServer(
            self,
            MoveDistance,
            'move_distance',
            self.execute_callback
        )

    async def execute_callback(self, goal_handle):

        distance = goal_handle.request.distance

        self.get_logger().info(f'Move {distance} meters')

        feedback_msg = MoveDistance.Feedback()

        for i in range(1, 11):
            feedback_msg.remaining_distance = distance - (i * (distance / 10))
            goal_handle.publish_feedback(feedback_msg)

        goal_handle.succeed()

        result = MoveDistance.Result()
        result.success = True

        return result


def main(args=None):
    rclpy.init(args=args)
    node = MoveDistanceServer()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
    