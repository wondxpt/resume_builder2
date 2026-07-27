[app]

title = Resume Builder
package.name = resumebuilder
package.domain = com.wondxpt

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,ttf

version = 1.0

# NOTE: pymupdf (fitz) is intentionally NOT listed here — it does not build
# for Android via python-for-android. The app already falls back gracefully
# to the schematic template preview when fitz isn't available (see
# pdf_preview.py), so this is safe to omit. Everything else the app needs:
requirements = python3,kivy==2.3.0,kivymd==1.2.0,reportlab,pillow,plyer,android

orientation = portrait
fullscreen = 0

# Icon / splash screen — replace these with your own 512x512 (icon) and
# any-size (presplash) PNGs before building. Buildozer will error out if
# these files don't exist, so either add real ones or comment these two
# lines out to use the Kivy default icon while you're still testing.
icon.filename = %(source.dir)s/icon.png
presplash.filename = %(source.dir)s/presplash.png

[android]

# Target/min API. 35 is the current Google Play minimum for new app
# submissions (as of 2026); this is required to move to 36 by
# Aug 31, 2026 — check the latest requirement at
# https://support.google.com/googleplay/android-developer/answer/11926878
# before your final release build and bump this if needed.
android.api = 35
android.minapi = 24
android.ndk = 25b

# Play Store requires 64-bit support at minimum.
android.archs = arm64-v8a, armeabi-v7a

# Photo picking via plyer's filechooser uses the system document/media
# picker (ACTION_OPEN_DOCUMENT), which does NOT require these permissions
# on modern Android — but they're included for older-device fallback paths.
android.permissions = READ_MEDIA_IMAGES, READ_EXTERNAL_STORAGE

# Required so the app can appear as a normal launcher app.
android.presplash_color = #FFFFFF

# Uses AndroidX (required for current Kivy/plyer/p4a recipes).
android.enable_androidx = True

# Increase if the build fails with an accept-licenses prompt.
android.accept_sdk_license = True

p4a.branch = master

[buildozer]
log_level = 2
warn_on_root = 1