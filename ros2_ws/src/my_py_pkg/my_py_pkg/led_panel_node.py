#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from my_robot_interfaces.msg import LedPanelState
from my_robot_interfaces.srv import SetLed

class LedPanelNode(Node): 
    def __init__(self):
        super().__init__("led_panel")
        self.battery_state = [0,0,0]
        self.led_state_publisher = self.create_publisher(LedPanelState, "led_panel_state", 10)
        self.timer_ = self.create_timer(0.5, self.publish_led_state)
        self.set_led_server = self.create_service(SetLed, "set_led", self.set_battery_state)
        self.get_logger().info("Led Panel Node Started")

    def publish_led_state(self):
        msg = LedPanelState()
        msg.state = self.battery_state
        self.led_state_publisher.publish(msg)
        self.get_logger().info(str(msg))

    def set_battery_state(self, request: SetLed.Request, response: SetLed.Response):
        if (request.set_state):
            self.battery_state = [0, 0, 1]
            response.success = True
        else:
            self.battery_state = [0, 0, 0]
            response.success = True

        return response




def main(args=None):
    rclpy.init(args=args)
    node = LedPanelNode() 
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()


