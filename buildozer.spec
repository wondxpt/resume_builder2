[app]

# Application title
title = Resume Builder

# Package name
package.name = resumebuilder

# Package domain
package.domain = com.wondxpt

# Source folder
source.dir = .

# Files to include
source.include_exts = py,png,jpg,jpeg,kv,atlas,ttf,json

# Version
version = 1.0.0

# Orientation
orientation = portrait


# Python requirements
requirements = python3,kivy==2.3.0,kivymd==1.2.0,reportlab==4.2.5,pillow==10.4.0,plyer,setuptools


# App icon
icon.filename = %(source.dir)s/assets/icon.png

# Splash
presplash.filename = %(source.dir)s/assets/presplash.png


# Architectures
android.archs = arm64-v8a,armeabi-v7a



[buildozer]

# Log level
log_level = 2



[android]

# Fullscreen
fullscreen = 0


# Android SDK API
android.api = 31


# Minimum Android version
android.minapi = 24


# NDK
android.ndk = 28c


# Enable AndroidX
android.enable_androidx = True


# Permissions
android.permissions = INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE


# Use p4a stable branch
p4a.branch = master


# Accept licenses
android.accept_sdk_license = True


# Java settings
android.gradle_dependencies = 


# Avoid old hostpython mismatch
android.hostpython3 = True



[python-for-android]

# Force modern host python
android.hostpython3 = True



[application]

# Main file
entrypoint = main.py
