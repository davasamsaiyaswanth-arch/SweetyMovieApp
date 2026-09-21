[app]
title = SweetyMovieApp
package.name = sweetyapp
package.domain = org.sweety.movie
source.dir =.
source.include_exts = py,png,jpg,kv,atlas,json
version = 0.1
requirements = python3,kivy==2.3.1,pillow==10.0.0,certifi,urllib3,charset-normalizer,idna,requests
orientation = portrait
android.permissions = INTERNET

[buildozer]
log_level = 2

p4a.fork = kivy
p4a.branch = develop
p4a.bootstrap = sdl2
android.api = 33
android.minapi = 24
android.ndk = 28c
android.build_tools_version = 33.0.2
android.accept_sdk_license_agreements = True
android.archs = arm64-v8a, armeabi-v7a
