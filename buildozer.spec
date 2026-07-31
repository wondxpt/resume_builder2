[app]
source.dir = .
title = Resume Builder
package.name = resumebuilder
package.domain = org.yourdomain
version = 1.0.0          # ← این نسخه‌ی اپلیکیشنه، نه Python!

requirements = python3,kivy==2.3.0,kivymd==2.0.0,pillow,plyer,setuptools   # ← python3 بدون عدد

orientation = portrait
icon.filename = icon.png
presplash.filename = presplash.png

android.api = 31
android.minapi = 21
android.ndk = 28c
android.permissions = INTERNET
p4a.branch = master       # ← این تغییر کرد

[buildozer]
log_level = 2
warn_on_root = 1
