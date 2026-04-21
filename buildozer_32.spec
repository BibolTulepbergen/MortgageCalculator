[app]
title = Mortgage Calculator
package.name = mortgagecalc
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.2
requirements = python3, kivy, kivymd, pillow, sdl2_ttf==2.0.15
orientation = portrait
osx.python_version = 3
osx.kivy_version = 1.9.1
icon.filename = %(source.dir)s/data/logo/logo.png
presplash.filename = %(source.dir)s/data/logo/tokio.jpg
fullscreen = 0
android.archs = armeabi-v7a
android.api = 31
android.minapi = 21
android.sdk = 31
android.accept_sdk_license = True
log_level = 2

[buildozer]
bin_dir = ./bin