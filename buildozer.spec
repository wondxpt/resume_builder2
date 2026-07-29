[app]

# (str) Title of your application
title = Resume Builder

# (str) Package name
package.name = resumebuilder

# (str) Package domain
package.domain = com.wondxpt

# (str) Source code where main.py is located
source.dir = .

# (str) Application version
version = 1.0.0

# (str) Application requirements
requirements = python3==3.11.7,kivy==2.3.0,kivymd==1.2.0,reportlab==4.0.9,pillow,plyer,android

# (str) Supported file extensions
source.include_exts = py,png,jpg,jpeg,kv,json,ttf,otf

# (str) Files/folders to exclude
source.exclude_exts = spec

# (str) Application orientation
orientation = portrait

# (bool) Fullscreen
fullscreen = 0

# (str) Application icon
icon.filename = %(source.dir)s/icon.png


# ------------------------------------------------------------------
# Android
# ------------------------------------------------------------------

# Android API
android.api = 34

# Minimum Android API
android.minapi = 24

# Android NDK
android.ndk = 25b

# Android architectures
android.archs = arm64-v8a,armeabi-v7a

# Debug build output
android.debug_artifact = apk

# Release build output
android.release_artifact = aab

# Android permissions
android.permissions = INTERNET

# AndroidX
android.enable_androidx = True

# Copy native libraries
android.copy_libs = 1


# ------------------------------------------------------------------
# python-for-android
# ------------------------------------------------------------------

# Use official Kivy python-for-android fork
p4a.fork = kivy

# IMPORTANT:
# Do NOT use "develop"
p4a.branch = v2024.01.21


# ------------------------------------------------------------------
# Build
# ------------------------------------------------------------------

log_level = 2
warn_on_root = 1
