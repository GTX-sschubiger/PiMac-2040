@echo off
title Subir PiMac 2040 a GitHub - SCHUBIGER.CL
color 0A
echo ========================================================
echo   PiMac 2040 - Subida a GitHub (SCHUBIGER.CL)
echo   Destino: https://github.com/GTX-sschubiger/PiMac-2040
echo ========================================================
echo.
cd /d "%~dp0"
if exist ".git" (
    echo [1/3] Carpeta git detectada en este directorio.
) else (
    echo [1/3] Entrando a carpeta github...
    cd github
)

echo [2/3] Configurando remote origin a GTX-sschubiger/PiMac-2040...
git remote set-url origin https://github.com/GTX-sschubiger/PiMac-2040.git 2>nul || git remote add origin https://github.com/GTX-sschubiger/PiMac-2040.git

echo [3/3] Subiendo rama main a GitHub...
echo (Si aparece una ventana en el navegador, autoriza el inicio de sesion con un clic)
echo.
git push -u origin main --force

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ========================================================
    echo   EXITO: El proyecto ha sido subido correctamente a:
    echo   https://github.com/GTX-sschubiger/PiMac-2040
    echo ========================================================
) else (
    echo.
    echo [AVISO] Si fallo, verifica tu conexion o autenticacion en el navegador.
)
echo.
pause
