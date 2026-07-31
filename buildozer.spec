[app]

# (str) Title of your application
title = Resume Builder


# (str) Package name
package.name = resumebuilder


# (str) Package domain
package.domain = com.wondxpt


# (str) Source code where the main.py live
source.dir = .


# (list) Source files to include
source.include_exts = py,png,jpg,jpeg,kv,atlas,ttf,json


# (str) Application version
version = 1.0.0


# (str) Supported orientation
orientation = portrait


# (list) Requirements
requirements = python3,kivy==2.3.0,kivymd==1.2.0,reportlab==4.2.5,pillow==10.4.0,plyer,setuptools


# (str) Presplash
presplash.filename = %(source.dir)s/assets/presplash.png


# (str) Icon
icon.filename = %(source.dir)s/assets/icon.png


# (list) Supported architectures
android.archs = arm64-v8a,armeabi-v7a



[buildozer]


# (int) Log level
log_level = 2



[android]


# (bool) Indicate if the application should be fullscreen
fullscreen = 0


# Android API
android.api = 31


# Minimum API
android.minapi = 24


# NDK version
android.ndk = 28c


# Enable AndroidX
android.enable_androidx = True


# Accept SDK licenses
android.accept_sdk_license = True


# Permissions
android.permissions = INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE


# Python-for-android branch
p4a.branch = master


# Backup old android tools issue fix
android.skip_update = False



[python-for-android]


# avoid old hostpython problems
android.hostpython3 = True



[application]


# Entry point
entrypoint = main.py
