# Metroid II Music Tools
This is a set of utilities made for dumping and importing music into Metroid II: Return of Samus.\
The script m2musdump.py extracts the music data as assembly code.\
The script patchsong.bat automatically handles writing a song back into the ROM.\
Writing a song back requires a properly set-up [RGBDS](https://github.com/rednex/rgbds/releases|RGBDS).\
Info on how the music code works can be seen commented in macros.asm.

QUICK TIPS:\
-Make sure your base rom is named "m2.gb".\
-If rgblink complains about one of the vanilla songs with an "Unable to place" error, go in the song file to where it's complaining and remove the instructions that overlap another section.
