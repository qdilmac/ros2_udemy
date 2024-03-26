#!/usr/bin/env python3

import rclpy
from rclpy import Node


class PyNodeOOP(Node): #inherit from Node object!
    def __init__(self):
        super.__init__("py_oop") #same as before. using self (Node) to create the node
        self.get_logger().info("Python OOP based Node [Recommended way to write nodes!]") #using self (Node) to access functions etc.


def main(args=None) -> None:
    rclpy.init(args=args)

    node = Node(PyNodeOOP)
    rclpy.spin(node)

    rclpy.shutdown()


if __name__ == "__main__":
    main()