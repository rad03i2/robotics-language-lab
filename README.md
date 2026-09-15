# Robotics Language Lab

A practical multi-language robotics playground that connects desktop software, embedded firmware, robot simulation, ROS-style configuration, telemetry, and control algorithms in one organized repository.

> This repository is built as a learning lab: every folder contains a small, readable robotics-related example instead of empty placeholder files.

## What this lab demonstrates

- Robot control basics: PID, sensor filtering, simple navigation, and diagnostics.
- Embedded thinking: Arduino, C, MicroPython, and hardware-style loops.
- Robotics software structure: ROS 2-style launch/config/URDF files.
- Telemetry and dashboards: JavaScript, TypeScript, Go, and C# examples.
- Systems programming practice: C++, Rust, and shell tooling.

## Languages and technologies

`Python` · `C++` · `C` · `Arduino` · `MicroPython` · `ROS 2` · `URDF` · `YAML` · `XML` · `JavaScript` · `TypeScript` · `C#` · `Go` · `Rust` · `Java` · `MATLAB/Octave` · `Shell` · `Docker`

## Repository map

```text
robotics-language-lab/
├── arduino/line_follower/          # Arduino line follower firmware
├── c/embedded/                     # Embedded C utilities
├── cpp/                            # C++ control and mapping examples
├── csharp/RobotDiagnostics/        # C# robot diagnostics CLI
├── docker/                         # Lightweight robotics dev container
├── docs/                           # Architecture and roadmap
├── go/telemetry-server/            # Go telemetry HTTP server
├── java/planner/                   # Java path planner example
├── javascript/dashboard/           # Browser dashboard demo
├── matlab/                         # MATLAB/Octave path smoothing
├── micropython/                    # MicroPython sensor script
├── python/                         # Sensors, control, navigation
├── ros2/                           # ROS 2-style package layout
├── rust/kinematics/                # Rust kinematics example
├── shell/                          # Simulation helper scripts
└── typescript/telemetry/           # Typed telemetry parser
```

## Quick examples

Run a Python PID controller demo:

```bash
python python/control/pid_controller.py
```

Run A* path planning:

```bash
python python/navigation/a_star.py
```

Run the Go telemetry server:

```bash
go run go/telemetry-server/main.go
```

Run the C# diagnostics example:

```bash
dotnet run --project csharp/RobotDiagnostics
```

Open the dashboard:

```bash
start javascript/dashboard/index.html
```

## Design idea

The project is intentionally small but broad. It is not claiming to be a complete production robot stack; it is a clean, organized robotics learning lab that shows how different languages can cooperate in one robot-oriented ecosystem.

## Focus areas

1. **Embedded firmware** for simple sensors and motors.
2. **Control algorithms** such as PID and filtering.
3. **Navigation algorithms** such as grid search and path planning.
4. **Robot description** using URDF-style structure.
5. **Telemetry** between a robot and dashboard/server tools.
6. **Developer tooling** for repeatable testing and simulation.

## Official links

- Portfolio: https://rdwan.dev
- Project page: https://rdwan.dev/projects/02-robotics-language-lab.html
