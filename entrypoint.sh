#!/bin/sh

## Start socat
su -m user -l -c 'socat tcp-l:9001,reuseaddr,fork EXEC:"/home/user/nebula-rogue"' &

## Start sshd
/usr/sbin/sshd -D 
