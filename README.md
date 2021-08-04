## Buffer overflow Windows exploit development practice - 50 proof of concepts

**What this repo is:**
After obtaining my OSCP, as preparation for my upcoming OSCE certification I challenged myself to re-write 50 proof of concepts for pre-existing exploits in software, all of which are Windows based.

NO looking at the original POC :persevere: no cheating

Secondly, this repo contains a handful of 0 days and CVE publications I have discovered and contributed while searching for new vulnerabilities in software.

Welcome to the early 2000's :)

----
I am writing 50 POC's for various exploits for educational purposes.

```
Exploits written : 29/50
Metasploit modules: 1
Metasploit contributions : 0
0day discoveries : 6
Assigned CVE's : 2
```

I would like to include but not be limited to : Vannila EIP overwrite, SEH + egghunters, ASLR/DEP/NX , SafeSeh, Stack cookies, unicode restrictions, and much more...

----
## Vanilla Stack Based Buffer Overflow

1. Vulnserver TRUN vanilla EIP overflow
2. FreeFloat FTP Server vanilla EIP overflow
3. PCMan FTP Server vanilla EIP overflow
4. Brainpan VulnHub box vanilla EIP overflow
5. DoStackBufferOverflowGood vanilla EIP overflow
6. MiniShare 1.4.1 vanilla EIP overflow
7. ASX to MP3 converter 3.1.2.1 vanilla EIP overflow
8. VUPlayer 2.49 .wax vanilla EIP overflow

----
## Structured Exception Handler (SEH) Overwrite + egghunter

  **Standard:**
  1. Easy File Sharing Web Server SEH overflow
  2. Millenium MP3 Studio 2.0 SEH overflow
  3. Free MP3 CD Ripper 2.6 SEH overflow
  4. RGUI i386 3.4.4 local SEH overflow
  5. Audiograbber 1.83 local SEH overflow
  6. 10-Strike Network Inventory Explorer SEH overflow
  
  **With egghunter:** [2004 whitepaper](http://www.hick.org/code/skape/papers/egghunt-shellcode.pdf)
  1. Easy File Sharing Web Server SEH overflow + egghunter
  2. Vulnserver GMON SEH overflow + egghunter
  3. Xitami Web Server 2.5 SEH overflow + egghunter + partial SEH overwrite

----
## Overflow Character restrictions
   **Unicode restrictions:** [2002 whitepaper](https://www.helpnetsecurity.com/dl/articles/unicodebo.pdf)
  1. GoldWave 5.70 local SEH + unicode bypass + Venetian alignment 
  2. CodeBlocks 17.12 local SEH + unicode bypass + Venetian alignment
   
   **Alphanumeric restrictions:**
  1. Vulnserver LTER vanilla EIP overflow + alphanumeric bypass
      
----
## ROP to bypass Data Execution Prevention (DEP)

1. Vulnserver TRUN + DEP enabled + ROP chain - VirtualProtect() method
2. ASX to MP3 converter 3.1.2.1 + DEP enabled + ROP chain - VirtualProtect() method
3. VUPlayer 2.49 + DEP enabled + ROP chain - VirtualProtect() method

----
## Vanilla EIP Heap spraying

1. RSP MP3 Player - OCX ActiveX EIP heap spray

----
## 0day discoveries / disclosures

1. [**exploit-db**](https://www.exploit-db.com/exploits/47410) DeviceViewer Sricam 3.12x local DOS buffer overflow
2. [**exploit-db**](https://www.exploit-db.com/exploits/47411) Easy File Sharing Web Server 7.2 SEH overflow 
3. [**CVE-2019-16724**](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-16724) File Sharing Wizard remote SEH overflow
4. [**CVE-2019-17181**](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-17181) IntraSrv webserver 1.0 SEH overflow

----
## Metasploit modules
   **Someone else contributing my exploits:**
   1. [*windows/http/file_sharing_wizard_seh*](https://www.rapid7.com/db/modules/exploit/windows/http/file_sharing_wizard_seh)
  
