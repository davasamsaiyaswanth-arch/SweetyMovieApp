
[app]

# Application name
title = SweetyMovieApp

# Package information
package.name = sweetyapp
package.domain = org.sweety.movie

# Source directory
source.dir = .

# Files included in the APK
source.include_exts = py,png,jpg,jpeg,kv,atlas,json

# Application version
version = 0.1

# Python and Kivy dependencies
requirements = python3==3.11.9,kivy==2.3.1,pyjnius

# Screen orientation
orientation = portrait

# Android permissions
android.permissions = INTERNET

# Supported architecture
android.archs = arm64-v8a

# Android SDK configuration
android.api = 35
android.minapi = 24
android.ndk = 25b

# Android build configuration
p4a.bootstrap = sdl2
p4a.fork = kivy
p4a.branch = master


[buildozer]

# Buildozer logging
log_level = 2

# Warn instead of failing if the user has not accepted licenses
android.accept_sdk_license = True
