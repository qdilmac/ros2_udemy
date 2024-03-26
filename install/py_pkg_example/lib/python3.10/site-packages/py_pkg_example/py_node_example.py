#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

def main(args=None) -> None:
    rclpy.init(args=args) #arguments from "main" func. will go in to arguments in rclpy.init, first line in every ros2 python program
    node = Node("py_example")
    node.get_logger().info("Hello ROS2 :]") # "hello world" in ROS2 :D
    rclpy.spin(node) # basically a loop function
    rclpy.shutdown() # last line in every ros2 python program.

if __name__ == "__main__":
    main()