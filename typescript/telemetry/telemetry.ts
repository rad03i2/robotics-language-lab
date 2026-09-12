type RobotStatus = 'ready' | 'moving' | 'standby' | 'error';

interface TelemetryPacket {
  robotId: string;
  batteryPercent: number;
  speedMetersPerSecond: number;
  headingDegrees: number;
  status: RobotStatus;
}

function parseTelemetry(json: string): TelemetryPacket {
  const packet = JSON.parse(json) as TelemetryPacket;

  if (!packet.robotId) throw new Error('robotId is required');
  if (packet.batteryPercent < 0 || packet.batteryPercent > 100) {
    throw new Error('batteryPercent must be between 0 and 100');
  }
  if (packet.headingDegrees < 0 || packet.headingDegrees >= 360) {
    throw new Error('headingDegrees must be in [0, 360)');
  }

  return packet;
}

const sample = parseTelemetry(JSON.stringify({
  robotId: 'mini-lab-bot-01',
  batteryPercent: 87,
  speedMetersPerSecond: 0.42,
  headingDegrees: 135,
  status: 'moving'
}));

console.log(sample);
