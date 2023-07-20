# Nebula Rogue - Format string Vulnerability

### Author: Emmmanuel

As intrepid space explorers, we embark on a journey through the intricate code cosmos woven by our junior dev, who crafted a mesmerizing FTP server for the homelabbers. Yet, before we unveil its full potential, we seek an audacious comrade like yourself to join our quest in unraveling any enigmatic anomalies that might lie within. Will you embark on this cosmic expedition with us?

# Vulnerabilty: Format string vulnerabilty
* During startup, a config is loaded which contains a ssh private key.
* For user input, they put in %p %p and so on to grab the SSH content from the stack.
* grab the ssh key, pivot to the next box

# Solution

There are two scripts

* fuzz.py: This is used to find all the address and values on the stack. For us, it turns out at index 43

* exploit.py: Returns a ssh private key to then ssh into the container

`Local solve: python3 exploit.py`

`Local debugging: python3 exploit.py GDB`

`Remote solve: python3 exploit REMOTE <IP> <PORT>`

## SETUP

```
# Build docker image
docker build -t format .

# Run image
docker run -p 2222:22 -p 9001:9001 format

```
