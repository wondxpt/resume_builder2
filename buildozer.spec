[app]

title = Resume Builder
package.name = resumebuilder
package.domain = com.wondxpt

source.dir = .
version = 1.0.0

requirements = python3==3.11.7,kivy==2.3.0,kivymd==1.2.0,pillow,plyer,android,reportlab

source.include_exts = py,png,jpg,jpeg,kv,json,ttf,otf,txt

source.exclude_exts = spec

source.exclude_dirs = .git,.github,.buildozer,bin


# --------------------------------------------------
# Application
# --------------------------------------------------

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

android.accept_sdk_license = True
android.skip_update = False

android.debug_artifact = apk
android.release_artifact = aab


# --------------------------------------------------
# Python-for-Android
# --------------------------------------------------

p4a.fork = kivy
p4a.branch = v2024.01.21

# Use our local ReportLab recipe instead of the broken
# built-in ReportLab recipe.
p4a.local_recipes = %(source.dir)s/p4a-recipes


# --------------------------------------------------
# Buildozer
# --------------------------------------------------

[buildozer]

log_level = 2
warn_on_root = 1
