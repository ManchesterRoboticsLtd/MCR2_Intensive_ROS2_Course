from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    talker_node = Node(package='basic_comms',
                       executable='talker',
                       output='screen'
                       )
    
    listener_node = Node(package='basic_comms',
                         executable='listener',
                         output='screen'
                         )
    
    l_d = LaunchDescription([talker_node,listener_node])

    return l_d