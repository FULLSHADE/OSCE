## Advanced Windows exploit development practice - 100 proof of concepts
----
I am writing 100 POC's for various exploits and corresponding advanced memory protections for education purposes.

```
Current status : 8/100
Metasploit contributions : 0
0day discoveries : 0
Assigned CVE's : 0
```

Including but not limited to : Vannila EIP overwrite, SEH + egghunters, ASLR/DEP/NX , SafeSeh, Stack cookies, and much more...

----
## Vanilla Stack Based Buffer Overflow

1. Vulnserver TRUN vanilla EIP overflow
2. FreeFloat FTP Server vanilla EIP overflow
2. PCMan FTP Server vanilla EIP overflow

----
## Structured Exception Handler (SEH) Overwrite + egghunter

1. Easy File Sharing Web Server SEH overflow
2. Easy File Sharing Web Server SEH overflow + egghunter
3. Xitami Web Server SEH overflow + egghunter + partial SEH overwrite
4. Vulnserver GMON SEH overflow + egghunter

----
## Using ROP to bypass Data Execution Prevention (DEP)

1. Vulnserver TRUN + DEP enabled + ROP chains bypass

----
## Bypassing ASLR

----
## Bypassing SafeSEH and SEHHOP

----
## Heap exploitation (and so it begins, let's stop being skids, eh?)

