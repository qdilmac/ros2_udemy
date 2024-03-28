#include "rclcpp/rclcpp.hpp"
#include "example_interfaces/msg/string.hpp" // dont forget to add dependencies in package.xml and CMakeLists.txt
                                             // should add node executable to the CMakeLists.txt also   

class RobotNewsStationNode : public rclcpp::Node
{
public:
    RobotNewsStationNode() : Node("robot_news_station"), robot_name("slim shady")
    {
        publisher = this->create_publisher<example_interfaces::msg::String>("robot_news", 10);
        timer = this->create_wall_timer(std::chrono::milliseconds(500),
                                        std::bind(&RobotNewsStationNode::publishMessage, this));
        RCLCPP_INFO(this -> get_logger(), "CPP Robot News Station has started.");
    }

private:
    void publishMessage()
    {
        auto msg = example_interfaces::msg::String();
        msg.data = std::string("Hi! My name is ") + robot_name + std::string("chkchkchk");
        publisher->publish(msg);
    }

    rclcpp::Publisher<example_interfaces::msg::String>::SharedPtr publisher;
    std::string robot_name;
    rclcpp::TimerBase::SharedPtr timer;
};

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<RobotNewsStationNode>();
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}