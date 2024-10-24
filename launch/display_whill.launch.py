from launch import LaunchDescription
from launch_ros.actions import Node
import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    urdf_file = os.path.join(
        get_package_share_directory('whill_description'),
        'urdf',
        'whill.urdf')

    rviz_config_file = os.path.join(
        get_package_share_directory('whill_description'),
        'rviz',
        'whill_urdf.rviz')

    return LaunchDescription([
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            arguments=[urdf_file],
            parameters=[{'use_sim_time': True}]
        ),
        # Node(
        #     package='rviz2',
        #     executable='rviz2',
        #     name='rviz2',
        #     output='screen',
        #     arguments=['-d', rviz_config_file]
        # ),
    ])
