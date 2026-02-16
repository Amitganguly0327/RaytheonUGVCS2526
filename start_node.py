from launch import LaunchDescription
import launch_ros.actions


def generate_launch_description():
    return LaunchDescription([
        launch_ros.actions.Node(
                        package="drone_control",
                        executable="start_node",
                        prefix="xterm -e gnome-terminal -- "),
        launch_ros.actions.Node(
                package="drone_control",
                executable="lidar_node",
                prefix="xterm -e gnome-terminal -- "),
        launch_ros.actions.Node(
                package="drone_control",
                executable="camera_node",
                prefix="xterm -e gnome-terminal -- "),
        launch_ros.actions.Node(
                package="drone_control",
                executable="perception_node",
                prefix="xterm -e gnome-terminal -- "),
        launch_ros.actions.Node(
                package="drone_control",
                executable="pathfinder_node",
                prefix="xterm -e gnome-terminal -- "),
        launch_ros.actions.Node(
                package="drone_control",
                executable="esc_node",
                prefix="xterm -e gnome-terminal -- "),
        launch_ros.actions.Node(
                package="drone_control",
                executable="radio_node",
                prefix="xterm -e gnome-terminal -- "),
        launch_ros.actions.Node(
                package="drone_control",
                executable="px4_interface_node",
                prefix="xterm -e gnome-terminal -- "),
        launch_ros.actions.Node(
                package="drone_control",
                executable="data_logging_node",
                prefix="xterm -e gnome-terminal -- "),
        launch_ros.actions.Node(
                package="drone_control",
                executable="kill_node",
                prefix="xterm -e gnome-terminal -- ")

    ])