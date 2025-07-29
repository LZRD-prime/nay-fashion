@echo off
REM Active l'environnement virtuel
call .venv\Scripts\activate.bat

REM Lance l'application Flask
python app.py

REM Garde la fenêtre ouverte après l'arrêt de l'application
pause