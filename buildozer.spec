[app]

title = Resume Builder
package.name = resumebuilder
package.domain = com.wondxpt

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,ttf,json

version = 1.0

# کتابخانه‌های مورد نیاز (بدون pymupdf)
requirements = python3,kivy==2.3.0,kivymd==1.2.0,reportlab,pillow,plyer,android

orientation = portrait
fullscreen = 0

# آیکون‌ها را کامنت کنید تا Buildozer از پیش‌فرض استفاده کند
# icon.filename = %(source.dir)s/icon.png
# presplash.filename = %(source.dir)s/presplash.png

[android]

# API جدیدتر (Google Play از آگوست ۲۰۲۴ به API 33+ نیاز دارد)
android.api = 33
android.minapi = 24
android.ndk = 25b

android.archs = arm64-v8a, armeabi-v7a

android.enable_androidx = True
android.permissions = INTERNET
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
