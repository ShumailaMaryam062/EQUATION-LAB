@echo off
REM EquationLab Standalone Frontend - No Server Required
REM Simply opens the HTML file directly in your default browser

cls
echo.
echo ============================================================
echo        EquationLab - Offline Frontend
echo ============================================================
echo.
echo Opening application in your browser...
echo.

cd /d "%~dp0"

REM Get the full path to index.html
set "filepath=%cd%\index.html"

REM Convert backslashes to forward slashes for file URL
setlocal enabledelayedexpansion
set "filepath=!filepath:\=/!"
set "url=file:///!filepath!"

REM Open in default browser
start "" "%url%"

echo.
echo ✅ Application opened in your browser!
echo.
echo If the browser doesn't open automatically:
echo Copy this path and open in your browser:
echo %url%
echo.
echo ============================================================
echo Features:
echo - No server required
echo - Works offline
echo - Real-time ODE solving
echo - Interactive plots
echo ============================================================
echo.
pause
