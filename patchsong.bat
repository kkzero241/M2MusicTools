@echo off

rem For this to work, open the music asm with this and make sure the rom is called "m2.gb".
rem Oh, and rgbds should be in hand.

echo Assembling specified song file...
rgbasm -o ".\%~n1.obj" %1
echo Patching m2.gb...
rgblink -O m2.gb -o ".\m2_%~n1.gb" ".\%~n1.obj"
echo Fixing the new rom's checksum...
rgbfix -f gh ".\m2_%~n1.gb"