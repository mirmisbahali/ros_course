#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from my_robot_interfaces.srv import SetLed


class BatteryNode(Node): 
    def __init__(self):
        super().__init__("battery")
        self.set_led = self.create_client(SetLed, "set_led")
        self.timer1 = self.create_timer(4, lambda: self.set_battery_state(False))
        self.timer2 = self.create_timer(6, lambda: self.set_battery_state(True))

    def set_battery_state(self, state):
        while not self.set_led.wait_for_service(1):
            self.get_logger().warn("Waiting for Led Panel Service")
        
        request = SetLed.Request()
        response = SetLed.Response()
        request.set_state = state
        future = self.set_led.call_async(request)

        if state:
            self.get_logger().info("Battery is Empty -> LED should turn on")
        else:
            self.get_logger().info("Battery is FULL -> LED should turn OFF")


        

        
        


def main(args=None):
    rclpy.init(args=args)
    node = BatteryNode() 
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()


