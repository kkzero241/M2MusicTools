import os

songtable_pos = int("11F30", 16) #Offsets to the songs themselves
flagtable_pos = int("11F70", 16) #Flags for each song determining stereo panning
songtable_list = [0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 0]
songtable_flags = [0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 0]

#Music note lists
clist = [0x2, 0x1a, 0x32, 0x4a, 0x62, 0x7a, 0x92] #C
csharplist = [0x4, 0x1c, 0x34, 0x4c, 0x64, 0x7c, 0x94] #Csharp
dlist = [0x6, 0x1e, 0x36, 0x4e, 0x66, 0x7e, 0x96] #D
dsharplist = [0x8, 0x20, 0x38, 0x50, 0x68, 0x80, 0x98] #Dsharp
elist = [0xa, 0x22, 0x3a, 0x52, 0x6a, 0x82, 0x9a] #E
flist = [0xc, 0x24, 0x3c, 0x54, 0x6c, 0x84, 0x9c] #F
fsharplist = [0xe, 0x26, 0x3e, 0x56, 0x6e, 0x86, 0x9e] #Fsharp
glist = [0x10, 0x28, 0x40, 0x58, 0x70, 0x88] #G
gsharplist = [0x12, 0x2a, 0x42, 0x5a, 0x72, 0x8a] #Gsharp
alist = [0x14, 0x2c, 0x44, 0x5c, 0x74, 0x8c] #A
asharplist = [0x16, 0x2e, 0x46, 0x5e, 0x76, 0x8e] #Asharp
blist = [0x18, 0x30, 0x48, 0x60, 0x78, 0x90] #B

#Parts of music sequences
noteoffset = 0
starttempo = 0
wordlist = []
loopoffset = 0

chn1offsets = []
chn2offsets = []
chn3offsets = []
chn4offsets = []

rom = open("m2.gb", "rb")

#Defines

#Cycles through the instructions lists
def parse_instruction_lists(offset):
    word = 0
    wordlist.clear()
    rom.seek(offset + 49152)
    while True:
        word = int.from_bytes(rom.read(2), byteorder='little')
        print(hex(rom.tell()))
        #print(hex(offset))
        #print(hex(word))
        wordlist.append(word)
        if word == 0xF0:
            return int.from_bytes(rom.read(2), byteorder='little')
            
        if word == 0xF0 or word == 0:
            return 0

def calc_note_difference(note):
    if noteoffset < 0x80:
        return note - noteoffset + (noteoffset & 1)
    else:
        return note + (256 - noteoffset) + (noteoffset & 1)

#Actually cycles the music instructions
def cycle_instructions(pos, channel):
    returnstring = ""
    currentbyte = 0
    patternbytes = 0
    rom.seek(pos + 49152)
    while True:
        currentbyte = int.from_bytes(rom.read(1), byteorder='little')
        patternbytes += 1
        #Check if end of pattern reached
        if currentbyte == 0:
            returnstring = returnstring + ("    endpattern\n    ;Total of " + str(patternbytes) + " bytes for this instruction pattern.\n")
            return returnstring
        #Check for sound disable
        elif currentbyte == 1:
            returnstring = returnstring + ("    haltsound\n")
        #Check for sound envelopes
        elif currentbyte == 3:
            returnstring = returnstring + ("    envelope 3\n")
        elif currentbyte == 5:
            returnstring = returnstring + ("    envelope 5\n")
        #Check for tempo tweaks
        elif currentbyte >> 4 == 0xA:
            returnstring = returnstring + ("    tweaktempo $" + str(currentbyte - 0xA0) + "\n")
        #Check for any F commands
        elif currentbyte == 0xF1:
            if channel == 1 or channel == 2:
                returnstring = returnstring + ("    initpulse $")
                returnstring = returnstring + (hex(int.from_bytes(rom.read(1), byteorder='little'))[2:] + ", $")
                returnstring = returnstring + (hex(int.from_bytes(rom.read(1), byteorder='little'))[2:] + ", $")
                returnstring = returnstring + (hex(int.from_bytes(rom.read(1), byteorder='little'))[2:] + "\n")
                patternbytes += 3
            elif channel == 3:
                returnstring = returnstring + ("    initwave $")
                returnstring = returnstring + (hex(int.from_bytes(rom.read(2), byteorder='little'))[2:] + ", $")
                returnstring = returnstring + (hex(int.from_bytes(rom.read(1), byteorder='little'))[2:] + "\n")
                patternbytes += 3
        elif currentbyte == 0xF2:
            returnstring = returnstring + ("    loadtempo $")
            returnstring = returnstring + (hex(int.from_bytes(rom.read(2), byteorder='little'))[2:] + "\n")
            patternbytes += 2
        elif currentbyte == 0xF3:
            returnstring = returnstring + ("    transpose $")
            returnstring = returnstring + (hex(int.from_bytes(rom.read(1), byteorder='little'))[2:] + "\n")
            patternbytes += 1
        elif currentbyte == 0xF4:
            returnstring = returnstring + ("    repeatinstructions $")
            returnstring = returnstring + (str(int.from_bytes(rom.read(1), byteorder='little')) + "\n")
            patternbytes += 1
        elif currentbyte == 0xF5:
            returnstring = returnstring + ("    repeatinstructionsend\n")
        #Check for actual music notes
        elif calc_note_difference(currentbyte) in clist:
            returnstring = returnstring + ("    C_ " + str(clist.index(calc_note_difference(currentbyte))) + "\n")
        elif calc_note_difference(currentbyte) in csharplist:
            returnstring = returnstring + ("    C# " + str(csharplist.index(calc_note_difference(currentbyte))) + "\n")
        elif calc_note_difference(currentbyte) in dlist:
            returnstring = returnstring + ("    D_ " + str(dlist.index(calc_note_difference(currentbyte))) + "\n")
        elif calc_note_difference(currentbyte) in dsharplist:
            returnstring = returnstring + ("    D# " + str(dsharplist.index(calc_note_difference(currentbyte))) + "\n")
        elif calc_note_difference(currentbyte) in elist:
            returnstring = returnstring + ("    E_ " + str(elist.index(calc_note_difference(currentbyte))) + "\n")
        elif calc_note_difference(currentbyte) in flist:
            returnstring = returnstring + ("    F_ " + str(flist.index(calc_note_difference(currentbyte))) + "\n")
        elif calc_note_difference(currentbyte) in fsharplist:
            returnstring = returnstring + ("    F# " + str(fsharplist.index(calc_note_difference(currentbyte))) + "\n")
        elif calc_note_difference(currentbyte) in glist:
            returnstring = returnstring + ("    G_ " + str(glist.index(calc_note_difference(currentbyte))) + "\n")
        elif calc_note_difference(currentbyte) in gsharplist:
            returnstring = returnstring + ("    G# " + str(gsharplist.index(calc_note_difference(currentbyte))) + "\n")
        elif calc_note_difference(currentbyte) in alist:
            returnstring = returnstring + ("    A_ " + str(alist.index(calc_note_difference(currentbyte))) + "\n")
        elif calc_note_difference(currentbyte) in asharplist:
            returnstring = returnstring + ("    A# " + str(asharplist.index(calc_note_difference(currentbyte))) + "\n")
        elif calc_note_difference(currentbyte) in blist:
            returnstring = returnstring + ("    B_ " + str(blist.index(calc_note_difference(currentbyte))) + "\n")
        #If it's somehow none of these, just do a db
        else:
            returnstring = returnstring + ("    db $" + hex(currentbyte)[2:] + "\n")

#Step 1: Gather all the song offsets
rom.seek(int("11F30", 16))
for i in range(32):
    songtable_list[i] = int.from_bytes(rom.read(2), byteorder='little')
    print(hex(songtable_list[i]))
#Step 2: Gather all the song stereo flags
for i in range(32):
    songtable_flags[i] = int.from_bytes(rom.read(1), byteorder='little')
    print(hex(songtable_flags[i]))

#Step 3: Begin dumping song data
for i in range(32):
    if i + 1 == 0x10: #Song 0x10 is just nothing, so skip over it
        continue
    
    rom.seek(songtable_list[i] + 49152)
    musfile = open("mus_0x" + hex(i + 1)[2:].zfill(2) + ".asm", "w")
    musfile.write(";Song 0x" + hex(i + 1)[2:].zfill(2))
    musfile.write("\n;Dumped with kkzero's Metroid II music dumper\n")
    musfile.write("\nINCLUDE \"macros.asm\"\n")
    musfile.write("\n;====================================================\n;SONG HEADER INFORMATION\n;====================================================\n")
    musfile.write("\nSONGPOS EQU $" + hex(songtable_list[i])[2:] + "\n")
    musfile.write("STEREOFLAG EQU $" + hex(songtable_flags[i])[2:] + "\n")
    musfile.write("\nSECTION \"SonglistPosition\",ROMX[$" + hex((songtable_pos + i * 2) - 49152)[2:].zfill(4) + "],BANK[4]\n")
    musfile.write("dw SONGPOS ;Reference to song's location in the songlist\n")
    musfile.write("\nSECTION \"FlaglistPosition\",ROMX[$" + hex((flagtable_pos + i) - 49152)[2:].zfill(4) + "],BANK[4]\n")
    musfile.write("db STEREOFLAG ;The byte determining how the song uses the stereo panning\n")
    musfile.write("\nSECTION \"SongHeader\",ROMX[SONGPOS],BANK[4]\n")
    noteoffset = int.from_bytes(rom.read(1), byteorder='little')
    musfile.write("\nNOTEOFFSET SET $" + hex(noteoffset)[2:].zfill(2) + "\n")
    musfile.write("Note_Offset::\n    db NOTEOFFSET\n")
    starttempo = int.from_bytes(rom.read(2), byteorder='little')
    musfile.write("Start_Tempo::\n    dw $" + hex(starttempo)[2:].zfill(4) + "\n")
    chn1list = int.from_bytes(rom.read(2), byteorder='little')
    chn2list = int.from_bytes(rom.read(2), byteorder='little')
    chn3list = int.from_bytes(rom.read(2), byteorder='little')
    chn4list = int.from_bytes(rom.read(2), byteorder='little')
    print(hex(chn1list))
    print(hex(chn2list))
    print(hex(chn3list))
    print(hex(chn4list))
    musfile.write("\n;Song instruction pointer lists\n")
    musfile.write("CHN1LIST EQU $" + hex(chn1list)[2:].zfill(4) + "\n")
    musfile.write("CHN2LIST EQU $" + hex(chn2list)[2:].zfill(4) + "\n")
    musfile.write("CHN3LIST EQU $" + hex(chn3list)[2:].zfill(4) + "\n")
    musfile.write("CHN4LIST EQU $" + hex(chn4list)[2:].zfill(4) + "\n")
    musfile.write("\ndw CHN1LIST, CHN2LIST, CHN3LIST, CHN4LIST\n")

    #Instruction lists are made and dealt with in this next sequence
    musfile.write("\n;====================================================\n;SONG INSTRUCTION LISTS\n;====================================================\n")
      
    if chn1list == chn2list:
        print(hex(i + 1) + " Case of Chn1 instructions equal to Chn2 instructions")
        if(chn1list != 0):
            musfile.write("\nSECTION \"PulseInstructionsList\",ROMX[CHN1LIST],BANK[4]\n")
            loopoffset = parse_instruction_lists(chn1list)
            k = 0
            print(str(loopoffset))
            for k in wordlist:
                print("k=" + str(hex(k)))

                if not k in chn1offsets and k != 0 and k != 240:
                    chn1offsets.append(k)
                
                if k != 0 and k != 240:
                    musfile.write("    dw $" + hex(k)[2:] + "\n")
                elif k == 0:
                    musfile.write("    endinstructionlist\n")
                elif k == 240:
                    musfile.write("    loopinstructionlist $" + hex(loopoffset)[2:] + "\n")
                    
    else:
        print(hex(i + 1) + " Chn1 and Chn2 are separate")
        if(chn1list != 0):
            musfile.write("\nSECTION \"Pulse1InstructionsList\",ROMX[CHN1LIST],BANK[4]\n")
            loopoffset = parse_instruction_lists(chn1list)
            k = 0
            print(str(loopoffset))
            for k in wordlist:
                print("k=" + str(hex(k)))
                
                if not k in chn1offsets and k != 0 and k != 240:
                    chn1offsets.append(k)
                
                if k != 0 and k != 240:
                    musfile.write("    dw $" + hex(k)[2:] + "\n")
                elif k == 0:
                    musfile.write("    endinstructionlist\n")
                elif k == 240:
                    musfile.write("    loopinstructionlist $" + hex(loopoffset)[2:] + "\n")
        if(chn2list != 0):
            musfile.write("\nSECTION \"Pulse2InstructionsList\",ROMX[CHN2LIST],BANK[4]\n")
            loopoffset = parse_instruction_lists(chn2list)
            k = 0
            print(str(loopoffset))
            for k in wordlist:
                print("k=" + str(hex(k)))
                
            
                if not k in chn2offsets and k != 0 and k != 240:
                    chn2offsets.append(k)
                
                if k != 0 and k != 240:
                    musfile.write("    dw $" + hex(k)[2:] + "\n")
                elif k == 0:
                    musfile.write("    endinstructionlist\n")
                elif k == 240:
                    musfile.write("    loopinstructionlist $" + hex(loopoffset)[2:] + "\n")
    if chn3list != 0:
        musfile.write("\nSECTION \"WaveInstructionsList\",ROMX[CHN3LIST],BANK[4]\n")
        loopoffset = parse_instruction_lists(chn3list)
        for k in wordlist:
                print("k=" + str(hex(k)))
                
            
                if not k in chn3offsets and k != 0 and k != 240:
                    chn3offsets.append(k)
                
                if k != 0 and k != 240:
                    musfile.write("    dw $" + hex(k)[2:] + "\n")
                elif k == 0:
                    musfile.write("    endinstructionlist\n")
                elif k == 240:
                    musfile.write("    loopinstructionlist $" + hex(loopoffset)[2:] + "\n")
    if chn4list != 0:
        musfile.write("\nSECTION \"NoiseInstructionsList\",ROMX[CHN4LIST],BANK[4]\n")
        loopoffset = parse_instruction_lists(chn4list)
        for k in wordlist:
                print("k=" + str(hex(k)))
                
            
                if not k in chn4offsets and k != 0 and k != 240:
                    chn4offsets.append(k)
                
                if k != 0 and k != 240:
                    musfile.write("    dw $" + hex(k)[2:] + "\n")
                elif k == 0:
                    musfile.write("    endinstructionlist\n")
                elif k == 240:
                    musfile.write("    loopinstructionlist $" + hex(loopoffset)[2:] + "\n")

    #Now to deal with the music instructions themselves
    musfile.write("\n;====================================================\n;SONG INSTRUCTIONS\n;====================================================\n")

    if chn1list != chn2list:
        musfile.write("\n;PULSE CHANNEL 1\n")
    else:
        musfile.write("\n;PULSE CHANNEL\n")

    #Cycle channel 1 offsets
    for pos in chn1offsets:
        musfile.write("\nSECTION \"Pulse1Instructions_" + str(hex(pos)[2:]) + "\",ROMX[$" + hex(pos)[2:] + "],BANK[4]\n")
        if pos in chn2offsets:
            musfile.write(";NOTE: This one's used for Channel 2 as well!\n")
        musfile.write(cycle_instructions(pos, 1))

    #Cycle channel 2 offsets
    if chn1list != chn2list:
        musfile.write("\n;PULSE CHANNEL 2\n")
        for pos in chn2offsets:
            if not pos in chn1offsets:
                musfile.write("\nSECTION \"Pulse2Instructions_" + str(hex(pos)[2:]) + "\",ROMX[$" + hex(pos)[2:] + "],BANK[4]\n")    
                musfile.write(cycle_instructions(pos, 2))
            
    if chn3list != 0:
        musfile.write("\n;WAVE CHANNEL\n")

    #Cycle channel 3 offsets
    for pos in chn3offsets:
        musfile.write("\nSECTION \"WaveInstructions_" + str(hex(pos)[2:]) + "\",ROMX[$" + hex(pos)[2:] + "],BANK[4]\n")
        musfile.write(cycle_instructions(pos, 3))
        
    if chn4list != 0:
        musfile.write("\n;NOISE CHANNEL\n")

    #Cycle channel 4 offsets
    for pos in chn4offsets:
        musfile.write("\nSECTION \"NoiseInstructions_" + str(hex(pos)[2:]) + "\",ROMX[$" + hex(pos)[2:] + "],BANK[4]\n")
        musfile.write(cycle_instructions(pos, 4))
        
    #Clear offset lists for next song
    chn1offsets.clear()
    chn2offsets.clear()
    chn3offsets.clear()
    chn4offsets.clear()

    #We're done, close the file
    musfile.close()

rom.close()
