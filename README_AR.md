<div align="center">

<img src="assets/project-cover.svg" alt="Robotics Language Lab" width="100%" />
<img src="assets/project-logo.svg" alt="شعار Robotics Language Lab" width="92" />

# Robotics Language Lab — الدليل العربي

**مختبر عملي متعدد اللغات لدراسة طبقات الروبوتات من الحساسات إلى التحكم والملاحة والقياس عن بُعد.**

[![CI](https://github.com/rad03i2/robotics-language-lab/actions/workflows/ci.yml/badge.svg)](https://github.com/rad03i2/robotics-language-lab/actions/workflows/ci.yml)

**[الصفحة الرئيسية](README.md) · [English](README_EN.md) · [المعمارية](docs/ARCHITECTURE.md) · [الأمان](SECURITY.md)**

</div>

---

<div dir="rtl" align="right">

## فكرة المشروع

هذا المستودع ليس تطبيق روبوت واحدًا، بل مختبر تعليمي يجمع أمثلة صغيرة وقابلة للفحص توضّح كيف تتوزع مهام الروبوت بين البرمجيات المضمنة والتحكم والملاحة ووصف الروبوت والقياس عن بُعد والتشخيص وأدوات التطوير.

## ما الموجود فعليًا؟

- تحكم PID وملاحة A* وفلتر تكميلي للحساس IMU بلغة Python.
- PID وخريطة إشغال بلغة C++.
- Ring Buffer بلغة C للأنظمة المضمنة.
- مثال Line Follower لـ Arduino.
- مثال HC-SR04 باستخدام MicroPython.
- Kinematics لروبوت Differential Drive باستخدام Rust.
- مخطط مسار بسيط بلغة Java.
- Path Smoothing لـ MATLAB/Octave.
- ملفات بأسلوب ROS 2 تشمل الإعدادات وLaunch وURDF صغيرًا.
- خادم Go يعرض Telemetry تجريبية بصيغة JSON.
- مثال TypeScript لمعالجة Telemetry.
- Dashboard مستقلة بالمتصفح تولد بيانات Telemetry تجريبية محليًا.
- أداة تشخيص روبوت باستخدام C# و.NET 8.
- أدوات Docker وShell مساعدة.

## تشغيل سريع

</div>

```bash
git clone https://github.com/rad03i2/robotics-language-lab.git
cd robotics-language-lab
python python/control/pid_controller.py
python python/navigation/a_star.py
```

<div dir="rtl" align="right">

## القياس عن بُعد والمعاينة

شغّل مثال Go:

</div>

```bash
go run go/telemetry-server/main.go
```

<div dir="rtl" align="right">

يقدم بيانات JSON تجريبية على:

`http://localhost:8080/telemetry`

أما `javascript/dashboard/index.html` فهي حاليًا **لوحة مستقلة** تولّد بياناتها التجريبية داخل JavaScript ولا تتصل بخادم Go في النسخة الحالية.

## أوامر إضافية

</div>

```bash
dotnet run --project csharp/RobotDiagnostics
cargo run --manifest-path rust/kinematics/Cargo.toml
javac java/planner/RobotPlanner.java
python -m unittest discover -s tests -v
```

<div dir="rtl" align="right">

## الاختبارات وCI

تتحقق GitHub Actions حاليًا من:

- صياغة Python والاختبارات السلوكية عبر Python 3.10 و3.12 و3.13 على Ubuntu وWindows وmacOS.
- بناء أمثلة C وC++ المحددة.
- بناء مشروع C# باستخدام .NET 8.

هذه الفحوص لا تحاكي Arduino أو MicroPython الفعلي، ولا تدعي إجراء اختبار تكامل ROS 2 كامل.

## السلامة عند استخدام العتاد

قبل تشغيل أي مثال على روبوت فعلي:

- راجع الجهد ونوع اللوحة وأرجل التوصيل.
- تحقق من حدود التيار والمحركات.
- اختبر التحكم أولًا والمحركات مفصولة أو معزولة.
- أضف إيقاف طوارئ مناسبًا.
- لا تنقل قيم PID أو Pins من المثال إلى عتاد حقيقي دون مراجعة.
- تعامل مع الكود على أنه مثال تعليمي وليس نظام تحكم معتمد للسلامة.

## وثائق المشروع

- [معمارية المختبر](docs/ARCHITECTURE.md)
- [الهوية البصرية](docs/BRAND.md)
- [خارطة الطريق](docs/ROADMAP.md)
- [سياسة الأمان](SECURITY.md)
- [الدعم](SUPPORT.md)
- [المساهمة](CONTRIBUTING.md)
- [سجل التغييرات](CHANGELOG.md)
- [الترخيص](LICENSE)

## المطور

**رضوان عبدالهادي**  
**Radwan Abd alhady Ahmed**  
GitHub: [@rad03i2](https://github.com/rad03i2)

</div>
