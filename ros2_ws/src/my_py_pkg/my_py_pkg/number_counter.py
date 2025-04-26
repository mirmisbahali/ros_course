#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64

class NumberCounter(Node):
    def __init__(self):
        super().__init__("number_counter")
        self.counter = 0
        self.prev = 0
        self.subscriber_ = self.create_subscription(Int64, "number", self.callback_number, 10)
        self.publisher_ = self.create_publisher(Int64, "number_counter", 10)
        self.get_logger().info("Number counter has been started")

    def callback_number(self, msg: Int64):
        if (self.prev == 0):
            self.prev = msg.data
        elif (self.prev != msg.data):
            self.counter += 1
            newmsg = Int64()
            newmsg.data = self.counter
            self.publisher_.publish(newmsg)
        self.get_logger().info(f'Counter = {self.counter}')
    
    def callback_number_publisher(self, msg: Int64):
        self.publisher_.publish(msg)
        


def main(args=None):
    rclpy.init(args=args)
    node = NumberCounter()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()