[app]

title = Resume Builder

package.name = resumebuilder

package.domain = com.wondxpt

source.dir = .

source.include_exts = py,png,jpg,jpeg,kv,atlas,ttf,json

version = 1.0.0

orientation = portrait


requirements = python3,kivy==2.3.0,kivymd==1.2.0,reportlab==4.2.5,pillow==10.4.0,plyer,setuptools



[android]

android.api = 35

android.minapi = 24

android.ndk = 28c

android.archs = arm64-v8a,armeabi-v7a

android.enable_androidx = True

android.build_tools_version = 35.0.0


android.permissions = INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE



[buildozer]

log_level = 2
