@ECHO off

CD C:\Users\Gal S\Documents\Projects\SaveMeHub
SET p=%1
SET p2=%2

IF "p2"=="ECHO is off."  (
    echo Im here
    python samehub.py %p%
) ELSE (
    echo %p% + %p2%
    python samehub.py %p% %p2%
)


