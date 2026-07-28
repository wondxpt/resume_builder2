[app]

# (str) Title of your application
title = Resume Builder

# (str) Package name
package.name = resumebuilder

# (str) Package domain
package.domain = com.wondxpt

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,jpeg,kv,atlas,ttf,json

# (str) Application version
version = 1.0

# (list) Application requirements
requirements = python3==3.11,kivy==2.3.0,kivymd==1.2.0,reportlab,pillow==10.4.0,plyer

# (str) Supported orientations
orientation = portrait

# (list) List of service to declare
services =


# (str) Icon of the application
# icon.filename = %(source.dir)s/assets/icon.png


# (str) Presplash
# presplash.filename = %(source.dir)s/assets/presplash.png



[buildozer]

# (int) Log level
log_level = 2


# (int) Display warning if buildozer is outdated
warn_on_root = 1


# (str) Path to build directory
build_dir = .buildozer


# (str) Path to bin directory
bin_dir = bin



[app:android]

# (bool) Indicate if the application should be fullscreen
fullscreen = 0


# (list) Permissions
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE


# (int) Android API
android.api = 31


# (int) Minimum API
android.minapi = 21


# (str) Android NDK version
android.ndk = 27.3.13750724


# (str) Android NDK path
# android.ndk_path =


# (str) Android architecture
android.archs = arm64-v8a,armeabi-v7a


# (bool)
android.accept_sdk_license = True


# (str) Android entry point
android.entrypoint = org.kivy.android.PythonActivity



# (list) Java classes
# android.add_src



# (bool) Use androidx
android.enable_androidx = True



# (str) Presplash background color
android.presplash_color = #FFFFFF



# (str) Backup rules
# android.allow_backup = True



[python-for-android]

# Avoid python 3.14 hostpython problem
p4a.branch = master

# Bootstrap
android.bootstrap = sdl2



[requirements]

# force versions
python_version = 3.11
