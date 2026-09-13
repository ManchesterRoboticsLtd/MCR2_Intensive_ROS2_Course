import rclpy
from rclpy.executors import ExternalShutdownException
from std_msgs.msg import String

g_node = None

def chatter_callback(msg):
    global g_node
    g_node.get_logger().info(
        'I heard: "%s"' % msg.data)


def main(args=None):
    global g_node
    rclpy.init(args=args)

    g_node = rclpy.create_node('minimal_subscriber')

    subscription = g_node.create_subscription(String, 'chatter', chatter_callback, 10)
    subscription  # prevent unused variable warning

    try:
        while rclpy.ok():
            rclpy.spin_once(g_node)

    except (KeyboardInterrupt, ExternalShutdownException):
        pass

    finally:
        if rclpy.ok():  # Ensure shutdown is only called once
            rclpy.shutdown()
        g_node.destroy_node()

if __name__ == '__main__':
    main()