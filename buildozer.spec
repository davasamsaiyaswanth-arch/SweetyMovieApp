
[app]

# Application name
title = SweetyMovieApp

# Package information
package.name = sweetyapp
package.domain = org.sweety.movie

# Application source
source.dir = .

# Main application file
source.main = main.py

# Included file extensions
source.include_exts = py,png,jpg,jpeg,kv,atlas,json

# Application version
version = 0.1

# Python dependencies
requirements = python3,kivy==2.3.1,pyjnius

# Screen orientation
orientation = portrait

# Internet permission
android.permissions = INTERNET

# Android architecture
android.archs = arm64-v8a

# Android API
android.api = 35
android.minapi = 24

# Android NDK
android.ndk = 25b

# Accept Android SDK licenses
android.accept_sdk_license = True

# Android bootstrap
p4a.bootstrap = sdl2

# Fullscreen
fullscreen = 0

# Log level
log_level = 2


[buildozer]

# Buildozer log level
log_level = 2

# Use python-for-android stable branch
p4a.branch = master
