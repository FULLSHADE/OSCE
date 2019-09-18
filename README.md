## Buffer overflow Windows exploit development practice - 50 proof of concepts

I am following the `Windows Exploit Development Tutorial Series` as a guide for exploit development progression from https://www.fuzzysecurity.com/tutorials.html

First I learn how to exploit a certain type of protections or restriction, then read lot's of exploits and writeups about it, then search exploit-db for software that is vulnerable to that specific attack vector, then I test my new knowledge against said software. 

Eventually I will start hunting for 0day in software that relates to these topics.

----
I am writing 50 POC's for various exploits, some which include bypassing advanced memory protections for educational purposes.

```
Current status : 11/100
Metasploit contributions : 0
0day discoveries : 0
Assigned CVE's : 0
```

Including but not limited to : Vannila EIP overwrite, SEH + egghunters, ASLR/DEP/NX , SafeSeh, Stack cookies, and much more...

----
## Vanilla Stack Based Buffer Overflow

1. Vulnserver TRUN vanilla EIP overflow
2. FreeFloat FTP Server vanilla EIP overflow
3. PCMan FTP Server vanilla EIP overflow
4. Brainpan VulnHub box vanilla EIP overflow
5. DoStackBufferOverflowGood vanilla EIP overflow
6. MiniShare 1.4.1 vanilla EIP overflow

----
## Structured Exception Handler (SEH) Overwrite + egghunter / and or restrictions

1. Easy File Sharing Web Server SEH overflow
2. Easy File Sharing Web Server SEH overflow + egghunter
3. Vulnserver GMON SEH overflow + egghunter
4. Xitami Web Server SEH overflow + egghunter + partial SEH overwrite

----
## Unicode Buffer Overflows

----
## Using ROP to bypass (DEP) and stack pivoting

1. Vulnserver TRUN + DEP enabled + ROP chains bypass

----
## Bypassing ASLR
