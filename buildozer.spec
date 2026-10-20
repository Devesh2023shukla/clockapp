[app]
title = ClockApp
package.name = clockapp
package.domain = org.devesh
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy
p4a.branch = v2024.01.21
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1

android.permissions = 
android.api = 33
android.minapi = 24
android.ndk = 25b
android.archs = arm64-v8a
