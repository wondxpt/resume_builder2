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
requirements = python3,kivy==2.3.0,kivymd==1.2.0,reportlab,pillow==10.4.0,plyer


# (str) Supported orientation
orientation = portrait


# (bool) Display fullscreen
fullscreen = 0



[buildozer]


# (int) Log level
log_level = 2


# (str) Warn if running as root
warn_on_root = 1



[android]


# (bool) Enable Android app
enable_android = True


# (str) Android API version
android.api = 31


# (str) Minimum Android API
android.minapi = 21


# (str) Android NDK version
android.ndk = 25b


# (str) Android SDK path
# automatically detected by GitHub Actions


# (list) Architectures
android.archs = arm64-v8a, armeabi-v7a


# (bool) Accept SDK licenses
android.accept_sdk_license = True


# (str) Android permissions
android.permissions = INTERNET



# (bool) Use androidx
android.enable_androidx = True
