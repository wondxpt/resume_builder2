[app]

# ===== اطلاعات پایه =====
title = Resume Builder
package.name = resumebuilder
package.domain = com.example
source.dir = .
version = 1.0.0
version.code = 1

# ===== وابستگی‌ها (بدون pillow برای جلوگیری از خطای کامپایل) =====
requirements = python3,kivy==2.3.0,kivymd==2.0.0,plyer,setuptools

# ===== تنظیمات اندروید =====
android.api = 31
android.ndk = 25c  # NDK 25c پایدارتر
android.minapi = 21
android.accept_sdk_license = True
android.archs = arm64-v8a, armeabi-v7a

# ===== مجوزها =====
android.permissions = INTERNET, ACCESS_NETWORK_STATE

# ===== متغیرهای محیطی برای رفع خطای ۵۰۲ =====
android.environment_variables = 
    P4A_FREETYPE_URL = https://sourceforge.net/projects/freetype/files/freetype2/2.14.1/freetype-2.14.1.tar.gz/download

# ===== تنظیمات دیگر =====
android.gradle = True
android.ndk_api = 21
android.allow_backup = True

# ===== اگر pillow مشکل داشت، این را اضافه کنید =====
# android.p4a_whitelist = pillow

[buildozer]
log_level = 2
warn_on_root = 1
