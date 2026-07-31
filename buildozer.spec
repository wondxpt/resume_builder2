[app]


title = Resume Builder


package.name = resumebuilder


package.domain = com.wondxpt


source.dir = .


source.include_exts = py,png,jpg,jpeg,kv,atlas,ttf,json


version = 1.0


requirements = python3==3.11.7,kivy==2.3.0,kivymd==1.2.0,reportlab==4.2.5,pillow==10.4.0,plyer,setuptools


orientation = portrait



[buildozer]


log_level = 2



[android]


android.api = 34


android.minapi = 24


android.ndk = 25b


android.archs = arm64-v8a,armeabi-v7a


android.enable_androidx = True


android.accept_sdk_license = True


android.permissions = INTERNET,READ_EXTERNAL_STORAGE



[python-for-android]


branch = develop
