[app]

# (نام و تنظیمات دیگر)

requirements = python3,kivy==2.3.0,kivymd==2.0.0,pillow,plyer,setuptools

# تنظیمات اندروید
android.accept_sdk_license = True
android.ndk = 28c
android.sdk = 37
android.minapi = 21
android.api = 31
android.arch = arm64-v8a, armeabi-v7a

# متغیرهای محیطی برای python-for-android (آدرس جایگزین)
android.environment_variables = 
    P4A_FREETYPE_URL = https://sourceforge.net/projects/freetype/files/freetype2/2.14.1/freetype-2.14.1.tar.gz/download

# سایر تنظیمات
android.allow_backup = True
android.permissions = INTERNET
android.manifest.add_hardware = android.hardware.touchscreen
