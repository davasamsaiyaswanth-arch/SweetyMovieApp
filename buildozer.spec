[app]
title = SweetyMovieApp
package.name = sweetyapp
package.domain = org.sweety.movie
source.dir =.
source.main = main.py
source.include_exts = py,png,jpg,jpeg,kv,atlas,json
version = 0.1
requirements = python3,kivy==2.3.1
orientation = portrait
android.permissions = INTERNET
android.archs = arm64-v8a
android.api = 33
android.minapi = 24
android.ndk = 25b
android.build_tools_version = 33.0.2
android.accept_sdk_license_agreements = True
p4a.bootstrap = sdl2
log_level = 2

[buildozer]
log_level = 2
