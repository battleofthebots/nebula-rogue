# Nebula Rogue - Format string Vulnerability

### Author: Emmanuel

As intrepid space explorers, we embark on a journey through the intricate code cosmos woven by our junior dev, who crafted a mesmerizing FTP server for the homelabbers. Yet, before we unveil its full potential, we seek an audacious comrade like yourself to join our quest in unraveling any enigmatic anomalies that might lie within. Will you embark on this cosmic expedition with us?

# Vulnerability: Format string vulnerability
* During startup, a config is loaded which contains a ssh private key.
* For user input, they put in %p %p and so on to grab the SSH content from the stack.
* grab the ssh key, pivot to the next box

# Static RE Challenges

* How many format modifiers do you need to obtain sensitive stack information? -> 115
* What is the FLAG offset -> 0x00104040
* What is the address of the vulnerable function? -> 0x001013c2

# Solution

There are a few ways to grab our sensitive information. 

First is by brute forcing. `fuzz.py` will send `%{index}$p` to the input and that will return an address pointer from the stack. Based on static analysis, we find out the FLAG offset has `040` as the last three bit. So check if the return address has that, if it does, it can be our possible target. Turns out the FLAG offset is on index `115` on the stack. After that, we will have to send `%115{$s}` to get the string content.

The second and more effective method is calculating the offset from _start. Using `exploit.py`, it uses the value `43` which returns the full `_start` address. After that, we subtract `0x001011a0 (_start offset)` from static analysis to get the base address of the program. With that, we can add `0x00104040 (Flag offset)` to get the exact address. From there, we send it over to the program to print out the content.

`Local solve: python3 exploit.py`

`Local debugging: python3 exploit.py GDB`

`Remote solve: python3 exploit.py REMOTE <IP> <PORT>`

## SETUP

```
# Build docker image
docker build -t format .

# Run image
docker run -p 2222:22 -p 9001:9001 format

```

## Extra challenge
The binary is also vulnerable to ret2lib. So if exploiting with format string is too easy, try the other method.
