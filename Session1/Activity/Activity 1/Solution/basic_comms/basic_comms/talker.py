# Imports
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

#Class Definition
class MinimalPublisher(Node):
    def __init__(self):
        super().__init__('talker_node')
        self.publisher = self.create_publisher(String, 'chatter', 10)
        timer_period = 0.5 #seconds
        self.timer = self.create_timer(timer_period, self.timer_cb)
        self.i = 0

    #Timer Callback
    def timer_cb(self):
        msg = String()
        msg.data = 'Hello World: %d' %self.i
        self.publisher.publish(msg)
        self.get_logger().info('Publising: "%s"' % msg.data)
        self.i +=1

#Main
def main(args=None):
    rclpy.init(args=args)

    minimal_publisher  = MinimalPublisher()

    try:
        rclpy.spin(minimal_publisher)
    except KeyboardInterrupt:
        pass
    finally:
        if rclpy.ok():  # Ensure shutdown is only called once
            rclpy.shutdown()
        minimal_publisher.destroy_node()


#Execute Node
if __name__ == '__main__':
    main()
