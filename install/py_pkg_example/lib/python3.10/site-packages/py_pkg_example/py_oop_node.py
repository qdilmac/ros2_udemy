#!/usr/bin/env python3

import rclpy
from rclpy.node import Node


class PyNodeOOP(Node): #inherit from Node object!
    def __init__(self):
        super().__init__("py_oop") #same as before. using self (Node) to create the node
        self.counter_ = 0
        self.get_logger().info("Python OOP based Node [Recommended way to write nodes!]") #using self (Node) to access functions etc.
        self.create_timer(0.5, self.timer_callback) #every 0.5 seconds, call timer_callback function
    
    def timer_callback(self):
        self.counter_ += 1
        self.get_logger().info(f"{self.counter_}. o_o/")


def main(args=None) -> None:
    rclpy.init(args=args)

    node = PyNodeOOP() # directly calling the class to do the job
    rclpy.spin(node)

    rclpy.shutdown()


if __name__ == "__main__":
    main()