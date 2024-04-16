#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from example_interfaces.srv import AddTwoInts
     
     
class SumIntsNode(Node):
    def __init__(self):
        super().__init__("sum_server")
        self.server = self.create_service(AddTwoInts, "sum_service", self.callback_sum_service) # service type, name of the service, callback function
        self.get_logger().info("Sum Server started!")

    def callback_sum_service(self, request, response):
        response.sum = request.a + request.b # AddTwoInts service requests 2 Int64 values and response is sum of those 2 Int64 values
                                            # int64a    int64 b ----   int64 sum 
        self.get_logger().info(str(request.a) + " + " + str(request.b) + " is equal to: " + str(response.sum))
        return response
     
def main(args=None): 
    rclpy.init(args=args)
    node = SumIntsNode()
    rclpy.spin(node)
    rclpy.shutdown()
    
     
if __name__ == "__main__":
    main()