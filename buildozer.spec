[app]

# (required) Title of your application
title = CalculatorApp

# (required) Package name of your application (com.example.myapp)
package.name = com.hecho.calculatorapp

# (required) Version of your application
package.version = 1.0

# (optional) Numeric version of your application
numeric.version = 1
version = 1

# (optional) Application author's name
author = HPaul Sweeney

# (optional) Application author's email
author.email = ypsweeney.ps@gmail.com

# (optional) Application icon (should be in the same directory as this file)
icon.filename = icon.png

# (required) Source code directory (can be '.', '../src', etc.)
source.dir = .

# (optional) Source code files (relative to source.dir)
source.include_exts = py,png,jpg,kv,atlas

# (optional) Additional files and folders to include (relative to the source directory)
# source.include_patterns = data/*,extra_files/*.txt

# (optional) List of directories to exclude from the build
# source.exclude_dirs = tests,bin

# (optional) List of packages to include (dependencies)
# requirements = kivy,requests

# (optional) List of packages to exclude from the build
# requirements_exclude = sqlite3

# (optional) URL for the application's main website
# homepage = https://example.com

# (optional) URL for the application's repository
# repository = https://github.com/example/calculatorapp.git

# (optional) Application entry point (main Python file)
# You should set this to the main Python file of your Kivy application
# For example: main.py, full_calc.py, etc.
entry_point = full_calc.py

# (optional) Presplash image (should be in the same directory as this file)
# presplash.filename = presplash.png

# (optional) Icon background color (in #RRGGBB format)
# icon.background_color = #FFFFFF

# (optional) Omit a loading spinner or not
# source.skip_loader = 1

# (optional) Android permissions to be granted to the application
# android.permissions = INTERNET

# (optional) Android features to be enabled in the application
# android.features = android.hardware.camera

# (optional) Minimum Android API version required by the application
# android.minapi = 21

# (optional) Target Android API version for the application
# android.api = 28

# (optional) Android SDK directory (if empty, it will be automatically detected)
# android.sdk = /path/to/android/sdk

# (optional) Android NDK directory (if empty, it will be automatically detected)
# android.ndk = /path/to/android/ndk

# (optional) Android NDK version to use
# android.ndk_version = 19b

# (optional) Python-for-Android branch to use
# p4a.branch = develop

# (optional) Whether to run `make clean` before compiling
# p4a.clean = 0

# (optional) Whether to bundle the Python interpreter in the APK
# p4a.preserve_main_python = 1

# (optional) Whether to strip debug symbols from compiled code
# p4a.strip = 1

# (optional) Custom Android manifest template (you can use this to add custom permissions, etc.)
# android.manifest = ./AndroidManifest.tmpl

# (optional) Custom buildozer.spec location
# spec = ./another_buildozer.spec

# (optional) List of source patterns to include in the final package
# include_patterns = assets/*,images/*.png

# (optional) List of source patterns to exclude from the final package
# exclude_patterns = licenses/*.txt

# (optional) Whether to generate a whitelist of permissions used by the application
# whitelist = ./whitelist.txt

# (optional) Whether to build for release or debug
# orientation = landscape

# (optional) Android-specific orientation
# package.domain = org.test
# package.domain = org.example
