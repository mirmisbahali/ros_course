#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64
from example_interfaces.srv import SetBool

class NumberCounter(Node):
    def __init__(self):
        super().__init__("number_counter")
        self.counter = 0
        self.prev = 0
        self.subscriber_ = self.create_subscription(Int64, "number", self.callback_number, 10)
        self.publisher_ = self.create_publisher(Int64, "number_count", 10)
        self.server_ = self.create_service(SetBool, "reset_counter", self.callback_reset_counter)
        self.get_logger().info("Number counter has been started")

    def callback_number(self, msg: Int64):
        self.counter += msg.data
        newmsg = Int64()
        newmsg.data = self.counter
        self.publisher_.publish(newmsg)

    def callback_reset_counter(self, request: SetBool.Request, response: SetBool.Response):
        if(request.data):
            self.counter = 0
            response.success = True
        else:
            response.success = False

        return response 

        


def main(args=None):
    rclpy.init(args=args)
    node = NumberCounter()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()