[app]

# Application title
title = Resume Builder

# Package name
package.name = resumebuilder

# Package domain
package.domain = com.wondxpt

# Source directory
source.dir = .

# Included file extensions
source.include_exts = py,png,jpg,jpeg,kv,atlas,ttf,json

# Version
version = 1.0

# Requirements
requirements = python3==3.11,kivy==2.3.0,kivymd==1.2.0,reportlab,pillow==10.4.0,plyer

# Orientation
orientation = portrait

# Fullscreen
fullscreen = 0


[buildozer]

# Log level
log_level = 2

# Don't stop for root warning
warn_on_root = 1


[android]

# Android API
android.api = 31

# Minimum Android API
android.minapi = 21

# Use NDK version compatible with Python 3.11
android.ndk = 25b

# Architectures
android.archs = arm64-v8a, armeabi-v7a

# Enable AndroidX
android.enable_androidx = True

# Permissions
android.permissions = INTERNET


# Java compile options
android.gradle_dependencies = androidx.appcompat:appcompat:1.6.1


[p4a]

# Avoid Python 3.14 problem
android.api = 31
