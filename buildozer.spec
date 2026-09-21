
[app]

# Application information
title = SweetyMovieApp
package.name = sweetyapp
package.domain = org.sweety.movie

# Source files
source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,json

# Version
version = 0.1

# Python and Kivy dependencies
requirements = python3==3.11.9,kivy==2.3.1,pyjnius

# Display settings
orientation = portrait
fullscreen = 0

# Android permissions
android.permissions = INTERNET

# Android architecture
android.archs = arm64-v8a

# Android API
android.api = 35
android.minapi = 24
android.ndk = 25b

# Python-for-Android configuration
p4a.fork = kivy
p4a.branch = master

# Bootstrap
p4a.bootstrap = sdl2

# Build settings
[buildozer]

log_level = 2
warn_on_root = 1
