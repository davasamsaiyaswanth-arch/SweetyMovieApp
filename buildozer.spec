
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

p4a.bootstrap = sdl2


[buildozer]

log_level = 2
warn_on_root = 1
