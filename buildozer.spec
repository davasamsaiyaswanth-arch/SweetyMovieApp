[app]

# App Name
title = SweetyMovieApp

# Package name
package.name = sweetyapp

# Domain
package.domain = com.sweety.movieapp

# Source dir
source.dir =.

# Include files
source.include_exts = py,png,jpg,kv,atlas,json,ttf
source.include_patterns = assets/*,images/*

# Version - SINGLE version only
version = 1.0

# Requirements - Python 3.11.9 FIX
requirements = hostpython3==3.11.9,python3==3.11.9,kivy,requests,urllib3,charset-normalizer,idna,certifi

# Orientation
orientation = portrait
fullscreen = 0

# Icon if you have
#icon.filename = %(source.dir)s/icon.png

[buildozer]

# Log level
log_level = 2

[app:android]

# Fix for Python 3.14 error - OLD STABLE BRANCH
p4a.fork = kivy
p4a.branch = v2023.12.24
p4a.bootstrap = sdl2

# Android settings
android.permissions = INTERNET
android.api = 33
android.minapi = 24
android.ndk = 25b
android.build_tools_version = 33.0.2
android.accept_sdk_license_agreements = True
android.ant = auto
android.archs = arm64-v8a, armeabi-v7a

# Allow backup
android.allow_backup = True

# Build type

[app:ios]
# Not needed
android.api = 33
android.minapi = 24
android.ndk = 25b
android.build_tools_version = 33.0.2
android.accept_sdk_license_agreements = True
android.ant = auto
android.archs = arm64-v8a, armeabi-v7a
