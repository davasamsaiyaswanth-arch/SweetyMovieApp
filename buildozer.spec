
[app]

title = SweetyMovieApp
package.name = sweetyapp
package.domain = org.sweety.movie

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,json,txt

version = 0.1

requirements = python3,kivy==2.3.1,pyjnius

orientation = portrait
fullscreen = 0

android.permissions = INTERNET

android.archs = arm64-v8a

android.api = 35
android.minapi = 24
android.ndk = 25b

android.accept_sdk_license = True
android.skip_update = True

p4a.bootstrap = sdl2
p4a.fork = kivy
p4a.branch = master


[buildozer]

log_level = 2
warn_on_root = 1
