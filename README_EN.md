<div align="center">

<img src="assets/project-cover.svg" alt="Robotics Language Lab" width="100%" />
<img src="assets/project-logo.svg" alt="Robotics Language Lab logo" width="92" />

# Robotics Language Lab — English Guide

**Small, runnable robotics examples across multiple languages and layers.**

[![CI](https://github.com/rad03i2/robotics-language-lab/actions/workflows/ci.yml/badge.svg)](https://github.com/rad03i2/robotics-language-lab/actions/workflows/ci.yml)

**[Main README](README.md) · [العربية](README_AR.md) · [Architecture](docs/ARCHITECTURE.md) · [Safety](SECURITY.md)**

</div>

---

## Purpose

This repository is a robotics learning laboratory, not a single application. It demonstrates how control, navigation, embedded programming, robot description, telemetry, diagnostics and tooling can be expressed across different languages without hiding each concept inside a large framework.

## What is actually included

- Python PID control, A* navigation and complementary IMU filtering.
- C++ PID and occupancy-grid examples.
- Embedded C ring buffer.
- Arduino line follower example.
- MicroPython HC-SR04 distance example.
- Rust differential-drive kinematics.
- Java straight-line planner.
- MATLAB/Octave path smoothing.
- ROS 2-style package metadata, parameters, launch XML and a small URDF model.
- Go simulated telemetry HTTP endpoint.
- TypeScript telemetry parsing example.
- Standalone JavaScript telemetry dashboard.
- .NET 8 C# robot diagnostics example.
- Docker and shell development helpers.

## Quick start

```bash
git clone https://github.com/rad03i2/robotics-language-lab.git
cd robotics-language-lab
python python/control/pid_controller.py
python python/navigation/a_star.py
```

## Visual and telemetry examples

Run the Go server:

```bash
go run go/telemetry-server/main.go
```

It serves simulated JSON at `http://localhost:8080/telemetry`.

The browser demo at `javascript/dashboard/index.html` currently generates its own simulated telemetry locally. It is useful as a visual example, but it is not wired to the Go endpoint in the current repository.

## Selected commands

```bash
dotnet run --project csharp/RobotDiagnostics
cargo run --manifest-path rust/kinematics/Cargo.toml
javac java/planner/RobotPlanner.java
python -m unittest discover -s tests -v
```

Use the relevant native toolchain for Arduino, MicroPython, MATLAB/Octave, ROS 2 and TypeScript examples.

## CI coverage

GitHub Actions verifies Python syntax and behavior on a cross-platform Python matrix, compiles the included C/C++ examples on Ubuntu, and builds the C# diagnostics project with .NET 8.

The workflow does not claim physical hardware validation or complete ROS 2 integration testing.

## Safety

Hardware examples are starting points. Confirm pin mappings, voltages, current limits, timing, actuator behavior and emergency-stop design before using adapted code on a real robot.

Network examples are development references. Add authentication, TLS, authorization and deployment hardening before exposing adapted services outside a trusted lab.

## Documentation

- [Architecture](docs/ARCHITECTURE.md)
- [Brand identity](docs/BRAND.md)
- [Roadmap](docs/ROADMAP.md)
- [Security and safety](SECURITY.md)
- [Support](SUPPORT.md)
- [Contributing](CONTRIBUTING.md)
- [Changelog](CHANGELOG.md)
- [License](LICENSE)

## Author

**Radwan Abd alhady Ahmed**  
**رضوان عبدالهادي**  
GitHub: [@rad03i2](https://github.com/rad03i2)
