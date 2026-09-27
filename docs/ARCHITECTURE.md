# Robotics Language Lab Architecture

Robotics systems cross several layers. This repository keeps those layers visible and intentionally separates examples by concern and toolchain.

## Layer map

| Layer | Repository areas | Purpose |
|---|---|---|
| Hardware-facing firmware | `arduino/`, `c/`, `micropython/` | Sensors, simple motor behavior and embedded data handling |
| Sensing / filtering | `python/sensors/` | Convert noisy measurements into more useful state |
| Control | `python/control/`, `cpp/control/` | Convert target state and feedback into control output |
| Navigation / planning | `python/navigation/`, `cpp/navigation/`, `java/planner/` | Decide feasible or useful movement paths |
| Kinematics | `rust/kinematics/` | Translate robot motion into wheel-level quantities |
| Robot description | `ros2/urdf/` | Describe a small robot body and wheel joints |
| Runtime configuration | `ros2/config/`, `ros2/launch/` | Demonstrate parameter and launch organization |
| Telemetry | `go/`, `typescript/` | Represent and expose simulated robot state |
| Dashboard | `javascript/dashboard/` | Standalone browser simulation of telemetry state |
| Diagnostics | `csharp/` | Present robot-health information in a developer CLI |
| Numeric experimentation | `matlab/` | Path-processing example |
| Tooling | `docker/`, `shell/` | Repeatable development and helper flows |

## Conceptual data flow

```text
Physical world
    │
    ▼
Sensors / embedded firmware
    │
    ▼
Filtering / state estimate
    │
    ├──────────────► Telemetry ─────► Dashboard / diagnostics
    │
    ▼
Control loop
    │
    ▼
Navigation / motion decisions
    │
    ▼
Actuators
```

The folders are examples of pieces in that flow; the repository does not claim they are wired into one complete runtime.

## Important separation

### Go telemetry service

`go/telemetry-server/main.go` exposes a simulated JSON packet at `/telemetry`.

### JavaScript dashboard

`javascript/dashboard/` currently maintains its own simulated state in the browser. It does not fetch the Go endpoint in the current implementation.

Keeping this distinction explicit prevents the documentation from implying integration that does not exist yet.

## ROS 2 boundary

The `ros2/` directory demonstrates package metadata, parameters, launch XML and a small differential-drive URDF. It is useful for studying structure but is not a complete deployable robot application.

## Testing boundary

CI can verify code syntax, tests and selected builds. It cannot validate motor motion, sensor noise, electrical safety, timing under real load, mechanical constraints or full ROS/hardware integration.

## Design principles

- Keep examples small and inspectable.
- State hardware assumptions explicitly.
- Prefer deterministic examples when practical.
- Do not hide safety-sensitive assumptions.
- Do not represent roadmap ideas as implemented behavior.
- Avoid credentials, private device endpoints and personal telemetry.
