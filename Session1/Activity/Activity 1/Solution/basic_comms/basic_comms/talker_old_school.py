import rclpy
from rclpy.executors import ExternalShutdownException
from time import sleep
from std_msgs.msg import String


def main(args=None):
    try:
        rclpy.init(args=args)
        
        node = rclpy.create_node('minimal_publisher')

        publisher = node.create_publisher(String, 'topic', 10)

        msg = String()

        i = 0
        while rclpy.ok():
            msg.data = 'Hello World: %d' % i
            i += 1
            node.get_logger().info('Publishing: "%s"' % msg.data)
            publisher.publish(msg)
            sleep(0.5)  # seconds
    except (KeyboardInterrupt, ExternalShutdownException):
        pass

    finally:
        if rclpy.ok():  # Ensure shutdown is only called once
            rclpy.shutdown()
        node.destroy_node()


if __name__ == '__main__':
    main()