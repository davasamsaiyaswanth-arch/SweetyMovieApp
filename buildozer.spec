[app]
title = SweetyMovieApp
package.name = sweetyapp
package.domain = com.sweety.movieapp

source.dir =.
source.include_exts = py,png,jpg,kv,atlas,json,ttf

version = 1.0
version.regex = __version__ = ['"](.*)['"]
version.filename = %(source.dir)s/main.py

requirements = python3,kivy
orientation = portrait
fullscreen = 0

[app:android]
p4a.branch = v2024.01.21
p4a.bootstrap = sdl2
p4a.port = 8000

android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk = 33
android.ndk_api = 21
android.accept_sdk_license_agreements = True

android.permissions = INTERNET
android.archs = arm64-v8a, armeabi-v7a

[buildozer]
log_level = 2
warn_on_root = 1
