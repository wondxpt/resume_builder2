[app]

title = Resume Builder
package.name = resumebuilder
package.domain = com.wondxpt

source.dir = .
version = 1.0.0

requirements = python3==3.11.7,kivy==2.3.0,kivymd==1.2.0,reportlab==4.0.9,pillow,plyer,android

source.include_exts = py,png,jpg,jpeg,kv,json,ttf,otf
source.exclude_exts = spec

orientation = portrait
fullscreen = 0

icon.filename = %(source.dir)s/icon.png


# --------------------------------------------------
# Android
# --------------------------------------------------

android.api = 34
android.minapi = 24

android.ndk = 25b

android.archs = arm64-v8a,armeabi-v7a

android.permissions = INTERNET

android.enable_androidx = True
android.copy_libs = 1

android.debug_artifact = apk
android.release_artifact = aab

# Automatically accept Android SDK licenses
android.accept_sdk_license = True

# Do not skip SDK updates
android.skip_update = False


# --------------------------------------------------
# python-for-android
# --------------------------------------------------

p4a.fork = kivy
p4a.branch = v2024.01.21


# --------------------------------------------------
# Buildozer
# --------------------------------------------------

[buildozer]

log_level = 2
warn_on_root = 1
