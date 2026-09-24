"""Behavioral tests for the dependency-free Python robotics examples."""

import importlib.util
import math
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


def load_module(name: str, relative: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / relative)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load {relative}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


pid_module = load_module("robotics_pid", "python/control/pid_controller.py")


class PIDControllerTests(unittest.TestCase):
    def test_proportional_response_has_expected_sign(self):
        controller = pid_module.PIDController(kp=2.0, ki=0.0, kd=0.0, setpoint=10.0)
        self.assertEqual(controller.update(measurement=7.0, dt=0.5), 6.0)
        self.assertLess(controller.update(measurement=12.0, dt=0.5), 0.0)

    def test_integral_accumulates_over_time(self):
        controller = pid_module.PIDController(kp=0.0, ki=1.0, kd=0.0, setpoint=2.0)
        self.assertAlmostEqual(controller.update(0.0, 0.5), 1.0)
        self.assertAlmostEqual(controller.update(0.0, 0.5), 2.0)

    def test_non_positive_dt_is_rejected(self):
        controller = pid_module.PIDController(kp=1.0, ki=0.0, kd=0.0, setpoint=1.0)
        for dt in (0.0, -0.1):
            with self.subTest(dt=dt):
                with self.assertRaises(ValueError):
                    controller.update(0.0, dt)

    def test_output_is_finite_for_normal_inputs(self):
        controller = pid_module.PIDController(kp=0.9, ki=0.05, kd=0.1, setpoint=1.0)
        output = controller.update(0.2, 0.1)
        self.assertTrue(math.isfinite(output))


if __name__ == "__main__":
    unittest.main()
