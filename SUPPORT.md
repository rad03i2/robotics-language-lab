# Robotics Language Lab Support

## Identify the example first

There is no single repository-wide runtime. Before troubleshooting, identify the folder and toolchain you are using.

Useful checks:

```bash
python --version
go version
dotnet --version
gcc --version
g++ --version
```

Only install or configure the toolchain required by the example you want to run.

## Python tests

```bash
python -m unittest discover -s tests -v
```

## Common questions

### The browser dashboard does not show data from the Go server

That is expected in the current version. The JavaScript dashboard generates its own simulated telemetry locally; the Go server is a separate telemetry endpoint example.

### A hardware example does not work on my board

Check board model, pin mapping, voltage level, sensor wiring, timing and library/runtime differences. The examples are educational starting points and cannot encode every hardware configuration.

### ROS 2 files do not launch a complete robot

The `ros2/` folder demonstrates package/configuration/URDF structure. It is not a complete robot application with all runtime nodes and hardware drivers.

### A compiler is missing

Use the toolchain for that folder only. The repository intentionally avoids a universal dependency installer because its examples target different runtimes.

## Bug reports

Include:

- operating system;
- language/runtime version;
- exact repository path;
- sanitized command;
- actual output;
- expected output;
- hardware model only when relevant and safe to share.

Never publish Wi-Fi passwords, camera URLs, robot credentials, SSH keys, broker credentials, cloud tokens or personal telemetry.

## Hardware safety

If the issue involves motors or physical movement, reproduce the problem with actuators disabled or mechanically isolated when possible.

Follow [SECURITY.md](SECURITY.md) for security and physical-safety guidance.

---

## الدعم بالعربية

هذا المستودع يحتوي أمثلة بعدة لغات، لذلك لا توجد طريقة تشغيل واحدة لكل المشروع. حدد المجلد واللغة أولًا، ثم تحقق من إصدار البيئة الخاصة بذلك المثال.

لا تنشر بيانات دخول الأجهزة أو الشبكات أو روابط كاميرات خاصة أو Telemetry شخصية في Issues العامة، واختبر تغييرات المحركات مع عزل الحركة الفعلية قدر الإمكان.
