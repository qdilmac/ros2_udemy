#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from example_interfaces.msg import String # dont forget to add dependencie for it in package.xml!

class NewsStationNode(Node):
    def __init__(self):
        super().__init__("news_station")

        self.robot_name = "BeepBoop"
        self.publisher_ = self.create_publisher(String, "robot_news", 10) # {message type}, {topic name}, {queue size}
        self.timer_ = self.create_timer(0.5, self.publish_news)
        self.get_logger().info("News station has been opened and started publishing very important news.") #just to check the node when we start it
    
    def publish_news(self):
        msg = String()
        msg.data = f"Hi my name is {self.robot_name} I am a topic that publishes this unneccessarily long message. No news here. You have been bamboozled."
        self.publisher_.publish(msg)
     
def main(args=None):
    rclpy.init(args=args)
    node = NewsStationNode()
    rclpy.spin(node)
    rclpy.shutdown()
    
     
if __name__ == "__main__":
    main()