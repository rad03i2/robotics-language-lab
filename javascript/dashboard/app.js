const telemetry = {
  battery: 96,
  speed: 0.0,
  heading: 0,
  status: 'ready'
};

function randomStep(value, amount, min, max) {
  const next = value + (Math.random() * amount * 2 - amount);
  return Math.max(min, Math.min(max, next));
}

function updateTelemetry() {
  telemetry.battery = Math.max(0, telemetry.battery - Math.random() * 0.8);
  telemetry.speed = randomStep(telemetry.speed, 0.08, 0, 1.2);
  telemetry.heading = (telemetry.heading + Math.random() * 20) % 360;
  telemetry.status = telemetry.speed > 0.05 ? 'moving' : 'standby';
  render();
}

function render() {
  document.querySelector('#battery').textContent = `${telemetry.battery.toFixed(1)}%`;
  document.querySelector('#speed').textContent = `${telemetry.speed.toFixed(2)} m/s`;
  document.querySelector('#heading').textContent = `${telemetry.heading.toFixed(0)}°`;
  document.querySelector('#status').textContent = telemetry.status;
}

document.querySelector('#tick').addEventListener('click', updateTelemetry);
render();
