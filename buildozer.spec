[app]

title = Resume Builder

package.name = resumebuilder

package.domain = com.wondxpt

source.dir = .

source.include_exts = py,png,jpg,jpeg,kv,atlas,ttf,json

version = 1.0


# Python 3.11 compatible packages
requirements = python3,kivy==2.3.0,kivymd==1.2.0,reportlab,pillow,plyer


orientation = portrait

fullscreen = 0



[buildozer]

log_level = 2

warn_on_root = 1



[android]

android.api = 31

android.minapi = 21


# Let GitHub Actions choose NDK
# android.ndk removed intentionally


android.archs = arm64-v8a,armeabi-v7a


android.enable_androidx = True


android.permissions = INTERNET


# prevent old build issues
android.accept_sdk_license = True



[p4a]

# Force Python version
python_version = 3.11
