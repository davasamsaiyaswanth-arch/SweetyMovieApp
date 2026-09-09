[app]
title = Sweety Movie Tracker
package.name = sweetymovieapp
package.domain = com.yashu.sweety
source.dir =.
source.include_exts = py,png
version = 0.1
requirements = python3,kivy
orientation = portrait
icon.filename = %(source.dir)s/icon.png

[buildozer]
log_level = 2

[app:android]
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk = 33
android.accept_sdk_license_agreements = True
android.ant = auto
p4a.bootstrap = sdl2
