[app]

# (str) Title of your application
title = Resume Builder

# (str) Package name
package.name = resumebuilder

# (str) Package domain
package.domain = com.wondxpt

# (str) Source code directory
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,jpeg,kv,atlas,ttf,json

# (str) Application version
version = 1.0

# (list) Application requirements
requirements = python3==3.11,kivy==2.3.0,kivymd==1.2.0,reportlab,pillow==10.4.0,plyer

# Force python version
android.python_version = 3.11

# (str) Supported orientation
orientation = portrait


# (bool) Copy library files
android.copy_libs = 1


# Android settings

[buildozer]

log_level = 2

warn_on_root = 1


# (str) Android API
android.api = 31

# Minimum Android version
android.minapi = 21

# NDK version compatible with buildozer
android.ndk = 25b

# Architecture
android.archs = arm64-v8a,armeabi-v7a


# Permissions

android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE


# Android theme
android.private_storage = True


# Avoid old cache problems
android.accept_sdk_license = True


# Debug mode
android.debug_artifact = apk


# Use gradle
p4a.branch = master
