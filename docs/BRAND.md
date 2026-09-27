# Robotics Language Lab Brand System

The repository uses a **Signal Matrix / Robotics Instrumentation** identity.

The visual idea is a robot placed inside a connected signal graph: sensors, control, navigation, embedded firmware, ROS-style structure and telemetry are separate nodes that exchange information.

## Core idea

**Many languages. One robot data flow.**

This matches the repository structure: the project is not a monolithic framework but a laboratory of independent examples that occupy different robotics layers.

## Palette

| Role | Name | Hex |
|---|---|---|
| Base | Lab midnight | `#101622` |
| Grid | Instrument slate | `#263247` |
| Primary signal | Electric lime | `#C8FF4D` |
| Sensor signal | Signal cyan | `#49D6FF` |
| Actuator signal | Actuator coral | `#FF6B57` |
| Telemetry signal | Telemetry magenta | `#F04FC2` |
| Light surface | Lab white | `#F3F7FC` |
| Muted text | Steel blue | `#AAB7CC` |

## Canonical assets

- `assets/project-cover.svg` — GitHub hero cover.
- `assets/project-logo.svg` — square identity mark.

## Logo construction

The mark combines:

- a compact robot head;
- five connected matrix nodes;
- colored signals for sensors, firmware, telemetry and control;
- a geometric frame that can remain legible at small sizes.

The full repository name should not be forced into the square logo.

## Visual language

1. Use connected nodes, instrumentation grids and signal paths.
2. Keep robot imagery geometric rather than cartoon-like.
3. Electric lime represents the main control/signal layer.
4. Cyan is used for sensing and data.
5. Coral is used for hardware and actuator-facing concepts.
6. Magenta is reserved for telemetry/ROS-style coordination.
7. Avoid generic AI brains, circuit-board stock art and photorealistic humanoid robots.

## README presentation

- The cover introduces the whole lab rather than one programming language.
- Current, runnable examples come before roadmap ideas.
- Hardware and safety boundaries must stay visible.
- Arabic and English detailed guides stay separate to avoid direction problems.
- The Go telemetry endpoint and JavaScript dashboard must be described as separate current examples until they are actually integrated.

## Character

The repository should feel like a **robotics instrumentation bench**: precise, experimental, technical and energetic, without pretending to be a production safety-certified stack.

---

**Developer:** رضوان عبدالهادي · Radwan Abd alhady Ahmed  
**GitHub:** [@rad03i2](https://github.com/rad03i2)
