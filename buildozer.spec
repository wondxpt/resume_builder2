[app]

title = Resume Builder

package.name = resumebuilder

package.domain = com.wondxpt

source.dir = .

source.include_exts = py,png,jpg,jpeg,kv,atlas,ttf,json

version = 1.0.0

requirements = python3,kivy==2.3.0,kivymd==1.2.0,reportlab==4.2.5,pillow,plyer

orientation = portrait


[buildozer]

log_level = 2


[android]

android.api = 31

android.minapi = 21

android.archs = arm64-v8a

android.enable_androidx = True
