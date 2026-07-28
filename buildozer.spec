[app]

# -----------------------------------------------------------------------------
# Basic app information
# -----------------------------------------------------------------------------
title = Resume Builder
package.name = resumebuilder
package.domain = com.wondxpt

# Source code and assets
source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,ttf,json

version = 1.0

# -----------------------------------------------------------------------------
# Requirements (libraries your app needs)
# NOTE: pymupdf (fitz) is NOT included because it doesn't build for Android.
# The app already handles missing fitz gracefully (see pdf_preview.py).
# -----------------------------------------------------------------------------
requirements = python3,kivy==2.3.0,kivymd==1.2.0,reportlab,pillow,plyer,android

orientation = portrait
fullscreen = 0

# -----------------------------------------------------------------------------
# Icon & splash screen – comment these out if you don't have the files yet.
# Buildozer will then use the Kivy default icon.
# -----------------------------------------------------------------------------
# icon.filename = %(source.dir)s/icon.png
# presplash.filename = %(source.dir)s/presplash.png

# -----------------------------------------------------------------------------
# Android specific settings
# -----------------------------------------------------------------------------
[android]

# Target SDK API level – Google Play requires at least 33 (as of Aug 2024)
android.api = 33

# Minimum supported Android version (Android 7.0+)
android.minapi = 24

# NDK version – stable and widely used
android.ndk = 25b

# Supported architectures – 64-bit is mandatory for Play Store
android.archs = arm64-v8a, armeabi-v7a

# Enable AndroidX (required by KivyMD and modern Android)
android.enable_androidx = True

# Permissions – INTERNET is used by some libraries; add others if needed
android.permissions = INTERNET

# Accept SDK licenses automatically (avoids interactive prompts)
android.accept_sdk_license = True

# -----------------------------------------------------------------------------
# Buildozer settings
# -----------------------------------------------------------------------------
[buildozer]

# Log level: 1 = normal, 2 = verbose (helps debug)
log_level = 2

# Warn if running as root – safe to ignore in GitHub Actions
warn_on_root = 1
