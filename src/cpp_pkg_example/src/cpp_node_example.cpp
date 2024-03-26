#include "rclcpp/rclcpp.hpp"

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<rclcpp::Node>("cpp_example");
    RCLCPP_INFO(node->get_logger(), "cpp is weird but np");
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}