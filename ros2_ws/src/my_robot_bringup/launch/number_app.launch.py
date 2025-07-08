from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    ld = LaunchDescription()

    number_publisher = Node(
        package="my_py_pkg",
        executable="number_publisher",
        name="my_number_publisher",
        remappings=[("/number", "/my_number")],
        parameters=[
            {"number": 12},
            {"timer_period": 1.3}
        ]
    )

    number_counter = Node(
        package="my_py_pkg",
        executable="number_counter",
        name="my_number_counter",
        remappings=[("/number", "/my_number")]
    )

    ld.add_action(number_publisher)
    ld.add_action(number_counter)

    return ld
