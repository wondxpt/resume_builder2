[app]

title = Resume Builder

package.name = resumebuilder

package.domain = com.wondxpt

source.dir = .

source.include_exts = py,png,jpg,jpeg,kv,atlas,ttf,json

version = 1.0.0

orientation = portrait


requirements = python3,kivy==2.3.0,kivymd==1.2.0,reportlab,pillow,plyer,setuptools


presplash.filename = %(source.dir)s/assets/presplash.png

icon.filename = %(source.dir)s/assets/icon.png



[buildozer]

log_level = 2



[android]

fullscreen = 0

android.api = 31

android.minapi = 24

android.ndk = 28c

android.enable_androidx = True

android.accept_sdk_license = True


android.permissions = INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE


android.archs = arm64-v8a



[python-for-android]

android.hostpython3 = True
