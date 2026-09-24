# Robotics Language Lab

A practical, multi-language robotics learning laboratory with runnable examples for control, navigation, embedded programming, telemetry, robot description, diagnostics, and developer tooling.

The repository deliberately favors small, inspectable programs over a pretend monolithic robot stack. Each example can be studied independently, while the folders demonstrate how common robotics concerns map across languages and runtimes.

## English

### Why this project exists
Robotics developers routinely cross boundaries between firmware, control code, desktop tooling, telemetry, simulation, and web interfaces. Robotics Language Lab provides a compact reference where those boundaries are visible without requiring a large framework just to explore an algorithm.

### Key features
- PID control examples and sensor-processing utilities.
- Grid/navigation examples, including A* path planning and occupancy-grid code.
- Arduino, embedded C, MicroPython, C++, Rust, Java, MATLAB/Octave, C#, Go, JavaScript and TypeScript examples.
- ROS 2-style configuration and robot-description assets for studying package structure.
- A lightweight Go telemetry service and browser dashboard example.
- Automated checks for Python, C and C++ plus Python behavioral tests.
- No API keys, cloud account, secrets, or paid services required.

### Preview guidance
This is primarily a code laboratory rather than a single GUI application. For a visual preview, run the Go telemetry server and open `javascript/dashboard/index.html`; for terminal previews, run the Python PID/A* examples or C# diagnostics command below. Hardware-oriented examples should be reviewed and adapted to your board and wiring before use.

### Requirements
You only need the toolchain for the example you want to run. Recommended baseline:
- Python 3.10+
- Go 1.22+ for the telemetry server
- .NET 8 SDK for C# diagnostics
- GCC/G++ with C++17 support for native examples
- A modern browser for the dashboard

Arduino, MicroPython, Rust, Java, MATLAB/Octave and ROS 2 are optional and only needed for their respective folders.

### Installation
```bash
git clone https://github.com/rad03i2/robotics-language-lab.git
cd robotics-language-lab
```

There is intentionally no repository-wide dependency installation: examples use their native toolchains and are kept independent.

### Usage
Python PID controller:
```bash
python python/control/pid_controller.py
```

A* navigation:
```bash
python python/navigation/a_star.py
```

Go telemetry service:
```bash
go run go/telemetry-server/main.go
```

C# diagnostics:
```bash
dotnet run --project csharp/RobotDiagnostics
```

Browser dashboard on Windows:
```powershell
start javascript/dashboard/index.html
```
On Linux/macOS, open that HTML file with your browser or a local static-file server.

### Configuration
Most examples expose constants close to the top of their source file so the relationship between configuration and behavior stays visible. Hardware pin assignments, ROS parameters, control gains, network addresses, and sensor assumptions must be reviewed before adapting an example to real hardware. Do not copy actuator limits or pin mappings blindly.

### Project structure
```text
arduino/                 Arduino firmware examples
c/                       Embedded C utilities
cpp/                     C++ control and navigation
csharp/                   Robot diagnostics CLI
docker/                   Lightweight development container
docs/                     Architecture and optional roadmap
go/                       Telemetry service
java/                     Planning example
javascript/               Browser dashboard
matlab/                   Path smoothing
micropython/              Sensor example
python/                   Control, sensors and navigation
ros2/                     ROS 2-style package/configuration examples
rust/                     Kinematics example
shell/                    Development/simulation helpers
tests/                    Behavioral tests
typescript/               Typed telemetry example
```

### Testing
Run the Python behavioral suite:
```bash
python -m unittest discover -s tests -v
```

GitHub Actions also performs Python syntax checks and compiles the checked C/C++ examples. Because this is a multi-toolchain lab, CI does not claim to emulate physical Arduino/MicroPython hardware or a complete ROS installation.

### Security and privacy
The repository does not require credentials and its examples do not intentionally collect personal data. Network examples are development references, not hardened internet-facing services. Bind experimental services to trusted interfaces, never commit camera/robot credentials, and apply authentication/TLS before exposing adapted services outside a local lab. See `SECURITY.md`.

### Limitations
- This is a learning/reference repository, not a certified robot-control stack.
- Hardware examples require board-specific pin, voltage, timing, and safety review.
- ROS assets illustrate structure and are not a complete deployable robot package.
- Telemetry/dashboard examples are intentionally lightweight and do not provide authentication, persistence, or fleet management.
- CI validates a useful subset of examples; it cannot validate physical sensors, motors, timing, or every optional toolchain.

### Optional roadmap
Future work may add hardware-in-the-loop examples, richer telemetry schemas, and additional tests for optional language toolchains. These are enhancements, not promises required for the current examples to run.

### Contributing
Small, runnable examples with clear assumptions are welcome. Keep examples focused, avoid secrets/generated artifacts, and document any new toolchain requirement. See `CONTRIBUTING.md`.

### License
MIT License. See `LICENSE`.

### Author
**Radwan Abdulhadi Ahmed**  
**رضوان عبدالهادي أحمد**  
GitHub: **@rad03i2**

---

## العربية

### نظرة عامة
**Robotics Language Lab** مختبر تعليمي عملي متعدد اللغات للروبوتات، يجمع أمثلة قابلة للتشغيل للتحكم والملاحة والبرمجة المضمنة والقياس عن بعد ووصف الروبوت والتشخيص وأدوات التطوير. الهدف هو تقديم أمثلة صغيرة وواضحة يمكن فهمها واختبارها منفردة بدل الادعاء بأنه نظام روبوتات إنتاجي متكامل.

### لماذا يوجد المشروع؟
مشاريع الروبوتات الحقيقية تجمع عادةً بين برمجيات المتحكمات، خوارزميات التحكم، أدوات سطح المكتب، الاتصالات، المحاكاة والواجهات. يوفر هذا المستودع مرجعًا منظمًا يوضح هذه الحدود بلغات مختلفة من دون فرض إطار ضخم على المتعلم.

### أهم الميزات
- أمثلة PID وأدوات معالجة بيانات الحساسات.
- أمثلة للملاحة والشبكات، ومنها تخطيط المسار A* وخرائط الإشغال.
- أمثلة Arduino وC وMicroPython وC++ وRust وJava وMATLAB/Octave وC# وGo وJavaScript وTypeScript.
- ملفات بأسلوب ROS 2 ووصف روبوت لدراسة بنية الحزم.
- خدمة Go خفيفة للقياس عن بعد ولوحة متصفح تجريبية.
- اختبارات سلوكية لبايثون وفحوص آلية لبناء أمثلة C/C++.
- لا يحتاج مفاتيح API أو حسابًا سحابيًا أو أسرارًا.

### المعاينة
المشروع مختبر أكواد أكثر من كونه تطبيق واجهة واحدة. للمعاينة المرئية شغّل خدمة Go وافتح `javascript/dashboard/index.html`. ويمكن تشغيل أمثلة PID وA* أو أداة C# لمعاينة النتائج في الطرفية. أمثلة العتاد يجب تكييفها مع اللوحة والتوصيلات قبل استخدامها فعليًا.

### المتطلبات والتثبيت
تحتاج فقط إلى بيئة اللغة الخاصة بالمثال المطلوب. يوصى بـ Python 3.10+ وGo 1.22+ و.NET 8 وGCC/G++ مع C++17 ومتصفح حديث. الأدوات الأخرى مثل Arduino وROS 2 وRust اختيارية بحسب المجلد.

```bash
git clone https://github.com/rad03i2/robotics-language-lab.git
cd robotics-language-lab
python python/control/pid_controller.py
python python/navigation/a_star.py
```

لا توجد عملية تثبيت موحدة للمستودع؛ فصل الأدوات مقصود حتى تبقى الأمثلة مستقلة وبسيطة.

### الإعداد
راجع الثوابت الموجودة في ملفات الأمثلة قبل التشغيل على عتاد حقيقي، خصوصًا أرجل التوصيل وحدود المحركات ومعاملات التحكم وعناوين الشبكة وافتراضات الحساسات. لا تنقل قيم العتاد إلى روبوت حقيقي من دون مراجعة هندسية مناسبة.

### بنية المشروع
المجلدات مقسمة حسب اللغة أو المجال: `python/` للتحكم والحساسات والملاحة، `cpp/` للتحكم والملاحة، `arduino/` للبرمجيات المضمنة، `ros2/` لملفات ROS، `go/` للقياس عن بعد، `javascript/` للوحة المتصفح، و`tests/` للاختبارات السلوكية، مع مجلدات اللغات الأخرى الموضحة في القسم الإنجليزي.

### الاختبارات
```bash
python -m unittest discover -s tests -v
```

تقوم GitHub Actions أيضًا بفحص صياغة Python وبناء أمثلة C وC++. هذه الفحوص لا تحاكي العتاد الحقيقي ولا تدعي اختبار جميع بيئات ROS أو المتحكمات.

### الأمان والخصوصية
لا يحتاج المشروع بيانات اعتماد ولا يجمع بيانات شخصية عمدًا. أمثلة الشبكة مخصصة للتعلم وليست خدمات جاهزة للإنترنت العام. استخدم شبكات موثوقة وأضف المصادقة وTLS عند تحويل أي مثال إلى خدمة فعلية، ولا ترفع بيانات دخول الكاميرات أو الروبوتات إلى المستودع. راجع `SECURITY.md`.

### القيود
المشروع ليس نظام تحكم معتمدًا للسلامة، وأمثلة العتاد تحتاج مراجعة للجهد والأرجل والتوقيت والحدود الميكانيكية. ملفات ROS توضيحية وليست حزمة روبوت مكتملة، ولوحة القياس لا توفر مصادقة أو تخزينًا دائمًا أو إدارة أسطول. كما أن CI لا يستطيع اختبار الحساسات والمحركات الفعلية.

### التطوير الاختياري
يمكن مستقبلًا إضافة اختبارات hardware-in-the-loop ومخططات telemetry أغنى واختبارات للغات الاختيارية. هذه تحسينات اختيارية وليست ميزات مزعومة حاليًا.

### المساهمة والترخيص
المساهمات التي تضيف أمثلة صغيرة قابلة للتشغيل وموثقة مرحب بها؛ راجع `CONTRIBUTING.md`. المشروع مرخص وفق MIT، والتفاصيل في `LICENSE`.

### المؤلف
**Radwan Abdulhadi Ahmed**  
**رضوان عبدالهادي أحمد**  
GitHub: **@rad03i2**
