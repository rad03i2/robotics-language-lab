# Architecture

Robotics projects usually combine many layers. This lab keeps the layers separate so each language has a useful role.

## Layers

| Layer | Example folders | Purpose |
|---|---|---|
| Firmware | `arduino/`, `c/`, `micropython/` | Read sensors and drive motors close to the hardware. |
| Control | `python/control/`, `cpp/control/` | Convert target values into motor commands. |
| Navigation | `python/navigation/`, `java/planner/`, `cpp/navigation/` | Decide where the robot should move next. |
| Robot model | `ros2/urdf/` | Describe the robot body, joints, and sensors. |
| Configuration | `ros2/config/`, `ros2/launch/` | Store runtime parameters and launch behavior. |
| Telemetry | `go/`, `typescript/`, `javascript/` | Move robot state into servers and dashboards. |
| Diagnostics | `csharp/` | Display robot health and status in developer tools. |
| Tooling | `shell/`, `docker/` | Make the project repeatable and easy to run. |

## Data flow

```text
Sensors → Filtering → State estimate → Control → Motor command
                       ↓
                 Telemetry server
                       ↓
                    Dashboard
```

## Safety note

This repository contains learning examples only. Real robots need proper limit checks, emergency-stop handling, hardware-specific drivers, and careful testing before movement.
