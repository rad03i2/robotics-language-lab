"""Simple PID controller demo for robotics control loops."""

from dataclasses import dataclass


@dataclass
class PIDController:
    kp: float
    ki: float
    kd: float
    setpoint: float
    integral: float = 0.0
    previous_error: float = 0.0

    def update(self, measurement: float, dt: float) -> float:
        if dt <= 0:
            raise ValueError("dt must be positive")

        error = self.setpoint - measurement
        self.integral += error * dt
        derivative = (error - self.previous_error) / dt
        self.previous_error = error
        return self.kp * error + self.ki * self.integral + self.kd * derivative


if __name__ == "__main__":
    pid = PIDController(kp=0.9, ki=0.05, kd=0.1, setpoint=1.0)
    position = 0.0

    for step in range(1, 16):
        command = pid.update(position, dt=0.1)
        position += command * 0.08
        print(f"step={step:02d} command={command:+.3f} position={position:.3f}")
