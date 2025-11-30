@echo off
set ZIPNAME=qbj3_milestone.zip

REM Remove old zip if it exists
if exist "%ZIPNAME%" del "%ZIPNAME%"

REM Create a temporary staging folder
set STAGE=package_stage
if exist "%STAGE%" rmdir /s /q "%STAGE%"
mkdir "%STAGE%"

REM Copy files/directories while preserving structure
xcopy "maps\qbj3_milestone.bsp" "%STAGE%\maps\" /i /s
xcopy "gfx\env\stick_sunset2_*.tga" "%STAGE%\gfx\env\" /i /s
xcopy "music\track250.ogg" "%STAGE%\music\" /i /s
xcopy "sound\qbj3_milestone" "%STAGE%\sound\qbj3_milestone\" /i /s /e
xcopy "txt\qbj3_milestone.txt" "%STAGE%\txt\" /i /s

REM Create zip file
powershell -command "Compress-Archive -Path '%STAGE%\*' -DestinationPath '%ZIPNAME%'"

REM Cleanup
rmdir /s /q "%STAGE%"

echo Done! Created %ZIPNAME%.
