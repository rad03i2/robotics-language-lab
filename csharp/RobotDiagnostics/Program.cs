namespace RobotDiagnostics;

record RobotHealth(string RobotId, double Battery, double CpuLoad, double MotorTemperature, string Status);

class Program
{
    static void Main()
    {
        var health = new RobotHealth("mini-lab-bot-01", 86.5, 34.2, 41.8, "Ready");

        Console.WriteLine("Robot Diagnostics");
        Console.WriteLine("-----------------");
        Console.WriteLine($"Robot: {health.RobotId}");
        Console.WriteLine($"Battery: {health.Battery:0.0}%");
        Console.WriteLine($"CPU Load: {health.CpuLoad:0.0}%");
        Console.WriteLine($"Motor Temperature: {health.MotorTemperature:0.0} C");
        Console.WriteLine($"Status: {health.Status}");
    }
}
