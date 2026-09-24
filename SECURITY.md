# Security Policy / سياسة الأمان

## English
Robotics Language Lab is an educational code repository, not a safety-certified robotics platform. If you discover a vulnerability in repository code, please report it privately through GitHub's security reporting features when available rather than publishing credentials, exploit details, or sensitive device information in a public issue.

### Safe use
- Treat all network-facing examples as development-only until you add authentication, authorization, TLS, rate limits, logging, and deployment hardening appropriate to your environment.
- Never store robot, camera, Wi-Fi, SSH, broker, or cloud credentials in source code.
- Test motor-control changes with actuators disabled or mechanically isolated first.
- Validate voltage levels, pin mappings, current limits, emergency-stop behavior, and physical clearances before connecting real hardware.
- Do not use these examples as the sole control layer for safety-critical machinery, vehicles, medical systems, or other systems where failure can cause harm.

Supported security fixes target the current default branch.

## العربية
هذا المستودع تعليمي وليس منصة روبوتات معتمدة للسلامة. عند اكتشاف ثغرة في كود المشروع، استخدم الإبلاغ الأمني الخاص في GitHub عندما يكون متاحًا بدل نشر بيانات حساسة أو تفاصيل استغلال في Issue عامة.

### الاستخدام الآمن
- اعتبر أمثلة الشبكة للتطوير المحلي إلى أن تضيف المصادقة والصلاحيات وTLS وحدود الطلبات والتسجيل والتحصين المناسب للنشر.
- لا تحفظ بيانات دخول الروبوت أو الكاميرا أو Wi-Fi أو SSH أو الوسطاء أو الخدمات السحابية داخل الكود.
- اختبر تغييرات التحكم بالمحركات أولًا والمحركات مفصولة أو معزولة ميكانيكيًا.
- تحقق من الجهد والأرجل وحدود التيار وإيقاف الطوارئ والمسافات الميكانيكية قبل توصيل عتاد حقيقي.
- لا تستخدم الأمثلة كطبقة التحكم الوحيدة في الأنظمة الحرجة للسلامة.
