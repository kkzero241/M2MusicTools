;Song 0x03
;Dumped with kkzero's Metroid II music dumper

;This is a dump of a custom song I wrote in raw hex
;around 9 months before the first release of m2musdump.
;It replaces the Chozo Ruins music.
;Evidently, it's a lot messier than any vanilla music track.
;Yes, it is an original composition.

INCLUDE "macros.asm"

;====================================================
;SONG HEADER INFORMATION
;====================================================

SONGPOS EQU $61d4
STEREOFLAG EQU $ff

SECTION "SonglistPosition",ROMX[$5f34],BANK[4]
dw SONGPOS ;Reference to song's location in the songlist

SECTION "FlaglistPosition",ROMX[$5f72],BANK[4]
db STEREOFLAG ;The byte determining how the song uses the stereo panning

SECTION "SongHeader",ROMX[SONGPOS],BANK[4]

NOTEOFFSET SET $01
Note_Offset::
    db NOTEOFFSET
Start_Tempo::
    dw $40df

;Song instruction pointer lists
CHN1LIST EQU $61df
CHN2LIST EQU $61f5
CHN3LIST EQU $6207
CHN4LIST EQU $0000

dw CHN1LIST, CHN2LIST, CHN3LIST, CHN4LIST

;====================================================
;SONG INSTRUCTION LISTS
;====================================================

SECTION "Pulse1InstructionsList",ROMX[CHN1LIST],BANK[4]
    dw $6219
    loopinstructionlist $61df

SECTION "Pulse2InstructionsList",ROMX[CHN2LIST],BANK[4]
    dw $62f6
    loopinstructionlist $61f5

SECTION "WaveInstructionsList",ROMX[CHN3LIST],BANK[4]
    dw $63df
    dw $6412
    dw $6435
    loopinstructionlist $6207

;====================================================
;SONG INSTRUCTIONS
;====================================================

;PULSE CHANNEL 1

SECTION "Pulse1Instructions_6219",ROMX[$6219],BANK[4]
    initpulse $50, $0, $80
    tweaktempo $3
    haltsound
    tweaktempo $2
    D# 1
    D# 1
    D# 1
    D# 1
    D# 1
    D# 1
    D# 1
    D# 1
    F# 1
    F# 1
    F# 1
    F# 1
    F# 1
    F# 1
    F# 1
    F# 1
    G# 1
    G# 1
    G# 1
    G# 1
    G# 1
    G# 1
    G# 1
    G# 1
    A# 1
    A# 1
    A# 1
    A# 1
    A# 1
    A# 1
    A# 1
    A# 1
    F# 1
    F# 1
    F# 1
    F# 1
    F# 1
    F# 1
    F# 1
    F# 1
    G# 1
    G# 1
    G# 1
    G# 1
    G# 1
    G# 1
    G# 1
    G# 1
    tweaktempo $1
    A# 1
    envelope 3
    haltsound
    haltsound
    haltsound
    haltsound
    haltsound
    haltsound
    haltsound
    haltsound
    haltsound
    haltsound
    haltsound
    haltsound
    haltsound
    haltsound
    haltsound
    haltsound
    haltsound
    haltsound
    haltsound
    haltsound
    haltsound
    haltsound
    haltsound
    haltsound
    haltsound
    haltsound
    haltsound
    haltsound
    haltsound
    haltsound
    endpattern
    ;Total of 89 bytes for this instruction pattern.

;PULSE CHANNEL 2

SECTION "Pulse2Instructions_62f6",ROMX[$62f6],BANK[4]
    initpulse $50, $0, $80
    tweaktempo $3
    haltsound
    tweaktempo $2
    D# 1
    D# 1
    D# 1
    D# 1
    D# 1
    D# 1
    D# 1
    D# 1
    F# 1
    F# 1
    F# 1
    F# 1
    F# 1
    F# 1
    F# 1
    F# 1
    G# 1
    G# 1
    G# 1
    G# 1
    G# 1
    G# 1
    G# 1
    G# 1
    A# 1
    A# 1
    A# 1
    A# 1
    A# 1
    A# 1
    A# 1
    A# 1
    F# 1
    F# 1
    F# 1
    F# 1
    F# 1
    F# 1
    F# 1
    F# 1
    G# 1
    G# 1
    G# 1
    G# 1
    G# 1
    G# 1
    G# 1
    G# 1
    tweaktempo $1
    A# 1
    envelope 3
    haltsound
    haltsound
    haltsound
    haltsound
    haltsound
    haltsound
    haltsound
    haltsound
    haltsound
    haltsound
    haltsound
    haltsound
    haltsound
    haltsound
    haltsound
    haltsound
    haltsound
    haltsound
    haltsound
    haltsound
    haltsound
    haltsound
    haltsound
    haltsound
    haltsound
    haltsound
    haltsound
    haltsound
    haltsound
    haltsound
    endpattern
    ;Total of 89 bytes for this instruction pattern.

;WAVE CHANNEL

SECTION "WaveInstructions_63df",ROMX[$63df],BANK[4]
    initwave $417b, $40
    tweaktempo $3
    haltsound
    tweaktempo $1
    D# 2
    envelope 3
    D# 1
    envelope 3
    haltsound
    haltsound
    haltsound
    haltsound
    D# 2
    envelope 3
    haltsound
    haltsound
    haltsound
    haltsound
    haltsound
    haltsound
    F# 2
    envelope 3
    F# 1
    envelope 3
    haltsound
    haltsound
    haltsound
    haltsound
    F# 2
    envelope 3
    haltsound
    haltsound
    haltsound
    haltsound
    haltsound
    haltsound
    endpattern
    ;Total of 40 bytes for this instruction pattern.

SECTION "WaveInstructions_6412",ROMX[$6412],BANK[4]
    G# 2
    envelope 3
    G# 1
    envelope 3
    haltsound
    haltsound
    haltsound
    haltsound
    G# 2
    envelope 3
    haltsound
    haltsound
    haltsound
    haltsound
    haltsound
    haltsound
    A# 2
    envelope 3
    F_ 2
    envelope 3
    haltsound
    haltsound
    haltsound
    haltsound
    D_ 2
    envelope 3
    haltsound
    haltsound
    haltsound
    haltsound
    haltsound
    haltsound
    endpattern
    ;Total of 33 bytes for this instruction pattern.

SECTION "WaveInstructions_6435",ROMX[$6435],BANK[4]
    tweaktempo $2
    F# 1
    envelope 3
    F# 1
    envelope 3
    F# 1
    envelope 3
    haltsound
    haltsound
    G# 1
    G# 1
    G# 1
    G# 1
    G# 1
    G# 1
    G# 1
    G# 1
    tweaktempo $2
    A# 1
    envelope 3
    haltsound
    haltsound
    haltsound
    haltsound
    haltsound
    haltsound
    tweaktempo $1
    A# 3
    envelope 3
    F_ 3
    envelope 3
    haltsound
    haltsound
    haltsound
    haltsound
    D_ 3
    envelope 3
    haltsound
    haltsound
    haltsound
    haltsound
    haltsound
    haltsound
    endpattern
    ;Total of 44 bytes for this instruction pattern.
