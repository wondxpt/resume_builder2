[app]

# 应用基本信息
title = Resume Builder
package.name = resumebuilder
package.domain = org.yourdomain

# 版本号
version = 1.0.0

# 核心依赖 (包含修复你之前问题的库)
requirements = python3,kivy==2.3.0,kivymd==2.0.0,pillow,plyer,setuptools,reportlab

# 界面设置
orientation = portrait

# 图标和启动画面 (请将your_icon.png和your_presplash.png替换为你的图片文件)
icon.filename = your_icon.png
presplash.filename = your_presplash.png

# ========== Android 特有设置 ==========
# 这些设置与云端构建环境兼容
android.api = 31
android.minapi = 21
android.ndk = 25b # 或 28c[reference:13]

# 权限
android.permissions = INTERNET

[buildozer]
log_level = 2
warn_on_root = 1
