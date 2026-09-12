#!/usr/bin/env bash
set -euo pipefail

echo "Robotics Language Lab simulation"
echo "--------------------------------"
echo "1) Checking Python examples"
python3 python/control/pid_controller.py >/dev/null || echo "Python example skipped"

echo "2) Showing sample robot telemetry"
echo '{"robotId":"mini-lab-bot-01","battery":91.5,"speed":0.42,"heading":120,"status":"simulated"}'

echo "3) Done"
