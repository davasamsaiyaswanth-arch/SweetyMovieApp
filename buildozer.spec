
[app]

title = SweetyMovieApp
package.name = sweetyapp
package.domain = org.sweety.movie

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,json

version = 0.1

requirements = python3,kivy==2.3.1,pyjnius

orientation = portrait

android.permissions = INTERNET

android.api = 35
android.minapi = 24
android.ndk = 25b
android.archs = arm64-v8a

android.accept_sdk_license = True

p4a.bootstrap = sdl2
p4a.fork = kivy
p4a.branch = master


[buildozer]

log_level = 2
