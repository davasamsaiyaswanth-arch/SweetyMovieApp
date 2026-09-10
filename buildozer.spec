[app]
title = Sweety Movie App
package.name = sweety.movie
package.domain = com.sweety.movie
source.dir =.
source.include_exts = py,png,jpg,kv,atlas,json
version = 1.0
requirements = python3,kivy==2.3.0,cython==3.0.0,pillow,certifi,urllib3,charset-normalizer,idna,requests
orientation = portrait

[app:android]
p4a.fork = kivy
p4a.branch = develop
p4a.bootstrap = sdl2

# Android settings
android.permissions = INTERNET
android.api = 33
android.minapi = 24
android.ndk = 28c
android.build_tools_version = 37.0.0
android.accept_sdk_license_agreements = True
android.ant = auto
android.archs = arm64-v8a

# Allow backup
android.allow_backup = True
