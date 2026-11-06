@echo off
setlocal enabledelayedexpansion

echo === Setting up Visual Studio Build Environment ===
call "C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Auxiliary\Build\vcvars64.bat"

set "PATH=C:\Antigravity\xpack-arm-none-eabi-gcc-13.3.1-1.1\bin;C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\Common7\IDE\CommonExtensions\Microsoft\CMake\Ninja;C:\Program Files\Git\cmd;%PATH%"
set "CMAKE=C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\Common7\IDE\CommonExtensions\Microsoft\CMake\CMake\bin\cmake.exe"

set "CC=cl.exe"
set "CXX=cl.exe"

if exist build rmdir /s /q build
mkdir build
cd build

echo === Running CMake ===
"%CMAKE%" -G Ninja -DPICO_SDK_PATH=C:/Antigravity/pico-sdk -DPICO_TOOLCHAIN_PATH=C:/Antigravity/xpack-arm-none-eabi-gcc-13.3.1-1.1/bin ..
if %ERRORLEVEL% NEQ 0 (
    echo CMake failed!
    exit /b %ERRORLEVEL%
)

echo === Building Firmware ===
"%CMAKE%" --build .
if %ERRORLEVEL% NEQ 0 (
    echo Build failed!
    exit /b %ERRORLEVEL%
)

echo === Build Succeeded! ===
