[app]
title = Mortgage Calculator
package.name = mortgagecalc
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.2
requirements = python3==3.11, kivy==2.3.0, kivymd==1.2.0, pillow, sdl2_ttf==2.0.15
orientation = portrait
osx.python_version = 3
osx.kivy_version = 1.9.1
icon.filename = %(source.dir)s/data/logo/logo.png
presplash.filename = %(source.dir)s/data/logo/tokio.jpg
fullscreen = 0
android.archs = arm64-v8a
android.api = 33
android.minapi = 24
android.sdk = 33
android.ndk = 25c
android.accept_sdk_license = True
android.gradle_dependencies = androidx.appcompat:appcompat:1.6.1
log_level = 2

[buildozer]
bin_dir = ./bin