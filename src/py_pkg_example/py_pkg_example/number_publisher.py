#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
    
from example_interfaces.msg import Int64
     
class NumberPublisherNode(Node):
    def __init__(self):
        super().__init__("number_publisher")
        self.number = 7
        self.number_publisher = self.create_publisher(Int64, "number", 10) #msg type, topic name, queue size
        self.number_timer = self.create_timer(1.0, self.publish_number)
        self.get_logger().info("Number publisher is up and running")

    def publish_number(self):
        msg = Int64()
        msg.data = self.number
        self.number_publisher.publish(msg)
     
     
def main(args=None):
    rclpy.init(args=args)
    node = NumberPublisherNode()
    rclpy.spin(node)
    rclpy.shutdown()
    
     
if __name__ == "__main__":
    main()