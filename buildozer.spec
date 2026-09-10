[app]
title = SweetyMovieApp
package.name = sweetyapp
package.domain = org.sweety.movie

source.dir =.
source.include_exts = py,png,jpg,kv,atlas,json,ttf
source.include_patterns = assets/*,images/*
version = 0.1
requirements = python3,kivy==2.3.1,cython==3.1.0,pillow==10.0.0,certifi,urllib3,charset-normalizer,idna,requests
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2

# Android
p4a.fork = kivy
p4a.branch = develop
p4a.bootstrap = sdl2
android.api = 33
android.minapi = 24
android.ndk = 28c
android.build_tools_version = 37.0.0
android.accept_sdk_license_agreements = True
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

# (Add permissions if needed)
# android.permissions = INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE
