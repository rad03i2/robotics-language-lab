#include <iostream>
#include <stdexcept>

class PIDController {
public:
    PIDController(double kp, double ki, double kd, double setpoint)
        : kp_(kp), ki_(ki), kd_(kd), setpoint_(setpoint) {}

    double update(double measurement, double dt) {
        if (dt <= 0.0) {
            throw std::invalid_argument("dt must be positive");
        }

        const double error = setpoint_ - measurement;
        integral_ += error * dt;
        const double derivative = (error - previous_error_) / dt;
        previous_error_ = error;
        return kp_ * error + ki_ * integral_ + kd_ * derivative;
    }

private:
    double kp_;
    double ki_;
    double kd_;
    double setpoint_;
    double integral_ = 0.0;
    double previous_error_ = 0.0;
};

int main() {
    PIDController pid(0.8, 0.04, 0.12, 10.0);
    double wheelSpeed = 0.0;

    for (int i = 0; i < 10; ++i) {
        const double command = pid.update(wheelSpeed, 0.1);
        wheelSpeed += command * 0.05;
        std::cout << "command=" << command << " wheelSpeed=" << wheelSpeed << '\n';
    }
}
