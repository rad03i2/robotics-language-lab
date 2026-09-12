"""Small complementary filter for IMU angle estimation."""

from dataclasses import dataclass


@dataclass
class ComplementaryFilter:
    alpha: float = 0.96
    angle: float = 0.0

    def update(self, accel_angle: float, gyro_rate: float, dt: float) -> float:
        gyro_angle = self.angle + gyro_rate * dt
        self.angle = self.alpha * gyro_angle + (1 - self.alpha) * accel_angle
        return self.angle


if __name__ == "__main__":
    filt = ComplementaryFilter()
    samples = [
        (1.2, 0.5),
        (1.4, 0.4),
        (1.8, 0.3),
        (2.0, 0.2),
    ]

    for accel_angle, gyro_rate in samples:
        print(round(filt.update(accel_angle, gyro_rate, dt=0.02), 4))
