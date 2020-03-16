;QUICK TIP: Macro calls need to be tabbed at a different column
;than its definition! Otherwise the assembler throws an error.

NOTEOFFSET SET 0

;Instruction list commands
loopinstructionlist:   MACRO
	dw $00F0, \1 ;Input is the offset in the list to loop from
ENDM

endinstructionlist:    MACRO
	dw $0000 ;Ends the playback of the instruction list, used for non-looping songs
ENDM

;Instructions commands
endpattern:			   MACRO
	db 0 ;Ends the instruction pattern
ENDM

haltsound:			   MACRO
	db 1 ;Cuts out any sound currently playing in the channel
ENDM

tweaktempo: 		   MACRO
	db $A0 | \1 ;Switches the tempo a little based on the offset the tempo was loaded from.
	;Used to simulate note durations.
ENDM

initpulse:			   MACRO
	db $F1, \1, \2, \3 ;Initializes the instrument to be played by a pulse channel.
ENDM

initwave:			   MACRO
	db $F1 ;Initializes the instrument to be played by the wave channel.
	dw \1
	db \2
ENDM

loadtempo:			   MACRO
	db $F2
	dw \1 ;The input value is an offset in the ROM containing tempo data
ENDM

transpose:			   MACRO
	db $F3, \1 ;Alters the pitch of the song
ENDM

repeatinstructions:    MACRO
	db $F4, \1 ;Repeats the next set of instructions for the specified amount
ENDM

repeatinstructionsend: MACRO
	db $F5 ;Encloses the loop started by the above macro
ENDM

envelope:			   MACRO
	db \1 ;The input value can only be 3 or 5
ENDM

;Music notes
C_: MACRO
	IF (NOTEOFFSET < $80) ;Put this check in because one song uses a noteoffset of $FE, which is treated the same as $02
		db $02 + ($18 * \1) + NOTEOFFSET - (NOTEOFFSET & 1) ;base note value + ($18 * note level) + noteoffset - if noteoffset is an odd number
	ELSE
		db $02 + ($18 * \1) - (256 - NOTEOFFSET) - (NOTEOFFSET & 1) ;base note value + ($18 * note level) - (256 - noteoffset) - if noteoffset is an odd number
	ENDC
ENDM

C#: MACRO
	IF (NOTEOFFSET < $80)
		db $04 + ($18 * \1) + NOTEOFFSET - (NOTEOFFSET & 1)
	ELSE
		db $04 + ($18 * \1) - (256 - NOTEOFFSET) - (NOTEOFFSET & 1)
	ENDC
ENDM

D_: MACRO
	IF (NOTEOFFSET < $80)
		db $06 + ($18 * \1) + NOTEOFFSET - (NOTEOFFSET & 1)
	ELSE
		db $06 + ($18 * \1) - (256 - NOTEOFFSET) - (NOTEOFFSET & 1)
	ENDC
ENDM

D#: MACRO
	IF (NOTEOFFSET < $80)
		db $08 + ($18 * \1) + NOTEOFFSET - (NOTEOFFSET & 1)
	ELSE
		db $08 + ($18 * \1) - (256 - NOTEOFFSET) - (NOTEOFFSET & 1)
	ENDC
ENDM

E_: MACRO
	IF (NOTEOFFSET < $80)
		db $0A + ($18 * \1) + NOTEOFFSET - (NOTEOFFSET & 1)
	ELSE
		db $0A + ($18 * \1) - (256 - NOTEOFFSET) - (NOTEOFFSET & 1)
	ENDC
ENDM

F_: MACRO
	IF (NOTEOFFSET < $80)
		db $0C + ($18 * \1) + NOTEOFFSET - (NOTEOFFSET & 1)
	ELSE
		db $0C + ($18 * \1) - (256 - NOTEOFFSET) - (NOTEOFFSET & 1)
	ENDC
ENDM

F#: MACRO
	IF (NOTEOFFSET < $80)
		db $0E + ($18 * \1) + NOTEOFFSET - (NOTEOFFSET & 1)
	ELSE
		db $0E + ($18 * \1) - (256 - NOTEOFFSET) - (NOTEOFFSET & 1)
	ENDC
ENDM

G_: MACRO
	IF (NOTEOFFSET < $80)
		db $10 + ($18 * \1) + NOTEOFFSET - (NOTEOFFSET & 1)
	ELSE
		db $10 + ($18 * \1) - (256 - NOTEOFFSET) - (NOTEOFFSET & 1)
	ENDC
ENDM

G#: MACRO
	IF (NOTEOFFSET < $80)
		db $12 + ($18 * \1) + NOTEOFFSET - (NOTEOFFSET & 1)
	ELSE
		db $12 + ($18 * \1) - (256 - NOTEOFFSET) - (NOTEOFFSET & 1)
	ENDC
ENDM

A_: MACRO
	IF (NOTEOFFSET < $80)
		db $14 + ($18 * \1) + NOTEOFFSET - (NOTEOFFSET & 1)
	ELSE
		db $14 + ($18 * \1) - (256 - NOTEOFFSET) - (NOTEOFFSET & 1)
	ENDC
ENDM

A#: MACRO
	IF (NOTEOFFSET < $80)
		db $16 + ($18 * \1) + NOTEOFFSET - (NOTEOFFSET & 1)
	ELSE
		db $16 + ($18 * \1) - (256 - NOTEOFFSET) - (NOTEOFFSET & 1)
	ENDC
ENDM

B_: MACRO
	IF (NOTEOFFSET < $80)
		db $18 + ($18 * \1) + NOTEOFFSET - (NOTEOFFSET & 1)
	ELSE
		db $18 + ($18 * \1) - (256 - NOTEOFFSET) - (NOTEOFFSET & 1)
	ENDC
ENDM