#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
     
from example_interfaces.msg import String

class SmartphoneNode(Node): 
    def __init__(self):
        super().__init__("smartphone")
        self.subscriber = self.create_subscription(String, "robot_news", 
                                                   self.callback_robot_news, 10) # msg type and topic name is very important! Should be same with publisher
        self.get_logger().info("You opened your smartphone for the 9854127. time today.") #msg type, topic name, callback func, queue size

    def callback_robot_news(self, msg): #callback_{topic_name} -> easy to understand which topic's callback it is
        self.get_logger().info(msg.data)
     
     
def main(args=None):
    rclpy.init(args=args)
    node = SmartphoneNode() 
    rclpy.spin(node)
    rclpy.shutdown()
    
     
if __name__ == "__main__":
    main()