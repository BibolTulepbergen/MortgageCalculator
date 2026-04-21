[app]

# Название твоего приложения в меню телефона
title = Mortgage Calculator

# Техническое имя (без пробелов)
package.name = mortgagecalc

# Твой "домен" (можешь оставить так)
package.domain = org.test

# Папка с кодом (точка значит текущая папка)
source.dir = .

# Расширения файлов, которые попадёт в APK
source.include_exts = py,png,jpg,kv,atlas

# ВЕРСИЯ ПРИЛОЖЕНИЯ
version = 0.2

# ЗАВИСИМОСТИ (Самое важное!)
# Здесь мы говорим сборщику скачать Python, Kivy и KivyMD
requirements = python3==3.11, kivy==2.3.0, kivymd==1.2.0, pillow, sdl2_ttf==2.0.15

# Ориентация экрана
orientation = portrait

# --- Android специфичные настройки ---

# (Сними решетку, если хочешь полноэкранный режим)
# fullscreen = 1

# Архитектура. Для большинства тестов на реальных телефонах оставь эту:
android.archs = armeabi-v7a

# Минимальная и целевая версия API Android (лучше не трогай)
android.api = 33
android.minapi = 24
android.sdk = 33
android.ndk = 25c
android.accept_sdk_license = True
android.gradle_dependencies = androidx.appcompat:appcompat:1.6.1

# Уровень логирования (2 — самый подробный, чтобы видеть ошибки)
log_level = 2

[buildozer]
# Папка, где Buildozer будет хранить скачанные файлы
bin_dir = ./bin

# Иконка приложения (логотип)
icon.filename = %(source.dir)s/data/logo/logo.png

# Заставка при запуске (сплэш-скрин)
presplash.filename = %(source.dir)s/data/logo/tokio.jpg