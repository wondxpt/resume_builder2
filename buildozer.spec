[app]

title = Resume Builder

package.name = resumebuilder

package.domain = com.wondxpt


source.dir = .


source.include_exts =
py,png,jpg,jpeg,kv,atlas,ttf,json



version = 1.0



requirements =
python3==3.11.7,
kivy==2.3.0,
kivymd==1.2.0,
pillow==10.4.0,
reportlab==4.2.5,
setuptools,
wheel



orientation = portrait



fullscreen = 0



[buildozer]

log_level = 2



[android]


android.api = 35

android.minapi = 24


android.ndk = 25b



android.archs =
arm64-v8a,armeabi-v7a



android.enable_androidx = True



android.accept_sdk_license = True



android.permissions =
READ_EXTERNAL_STORAGE,
WRITE_EXTERNAL_STORAGE



p4a.branch = master



[python-for-android]

android.private_storage = True
