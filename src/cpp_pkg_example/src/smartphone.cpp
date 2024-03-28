#include "rclcpp/rclcpp.hpp"
#include "example_interfaces/msg/string.hpp"

class SmartphoneNode : public rclcpp::Node
{
public:
    SmartphoneNode() : Node("smartphone")
    {
        subscriber = this->create_subscription<example_interfaces::msg::String>(
            "robot_news", 10,           // std::placeholder -> callback func. has 1 parameter. if more param (like 2 or more)
            std::bind(&SmartphoneNode::callbackRobotNews, this, std::placeholders::_1)); // change accordingly to the param number

        RCLCPP_INFO(this->get_logger(), "CPP Smartphone has been started.");
    }

private:
    void callbackRobotNews(const example_interfaces::msg::String::SharedPtr msg)
    {
        RCLCPP_INFO(this->get_logger(), "%s", msg->data.c_str());
    }

    rclcpp::Subscription<example_interfaces::msg::String>::SharedPtr subscriber;
};

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<SmartphoneNode>();
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}