#include "rclcpp/rclcpp.hpp"

class CppNodeOOP : public rclcpp::Node
{
public:
    CppNodeOOP() : Node("cpp_oop"), counter(0)
    {
        RCLCPP_INFO(this->get_logger(), "oop cpp abcdefg"); // instead of "node" we use "this"

        timer_ = this->create_wall_timer(std::chrono::seconds(1),
                                         std::bind(&CppNodeOOP::timerCallback, this));
    }

private:
    void timerCallback()
    {
        counter ++;
        RCLCPP_INFO(this->get_logger(), "i repeat o/ for the %d. time", counter);
    }

    rclcpp::TimerBase::SharedPtr timer_;
    int counter;
};

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<CppNodeOOP>();
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}