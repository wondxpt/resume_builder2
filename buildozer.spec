[app]
title = Resume Builder
package.name = resumebuilder
package.domain = com.example
source.dir = .
version = 1.0.0
version.code = 1
requirements = python3,kivy==2.3.0,kivymd==2.0.0,plyer,setuptools
android.api = 31
android.ndk = 28c
android.minapi = 21
android.accept_sdk_license = True
android.archs = arm64-v8a, armeabi-v7a
android.permissions = INTERNET, ACCESS_NETWORK_STATE
android.environment_variables = 
    P4A_FREETYPE_URL = https://sourceforge.net/projects/freetype/files/freetype2/2.14.1/freetype-2.14.1.tar.gz/download
android.gradle = True
android.ndk_api = 21
android.allow_backup = True

[buildozer]
log_level = 2
warn_on_root = 1
