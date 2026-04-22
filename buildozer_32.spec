[app]
title = Mortgage Calculator
package.name = mortgagecalc
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.2
requirements = python3==3.11,kivy==2.3.0,kivymd==1.2.0,pillow
orientation = portrait
icon.filename = %(source.dir)s/data/logo/logo.png
presplash.filename = %(source.dir)s/data/logo/tokio.jpg
fullscreen = 0

android.archs = armeabi-v7a
android.api = 33
android.minapi = 24
android.ndk = 25c
android.accept_sdk_license = True
android.gradle_dependencies = androidx.appcompat:appcompat:1.6.1,androidx.constraintlayout:constraintlayout:2.1.4
android.gradle_options = org.gradle.jvmargs=-Xmx2048m,org.gradle.parallel=true
android.permissions = INTERNET
android.entrypoint = org.kivy.android.PythonActivity
android.bootstrap = sdl2

log_level = 2
warn_on_root = 1

[buildozer]
log_level = 2
bin_dir = ./bin
warn_on_root = 1