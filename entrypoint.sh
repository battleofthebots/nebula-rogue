#!/bin/sh

## Start socat
socat tcp-l:9001,reuseaddr,fork EXEC:"/home/user/format" &

## Start sshd
/usr/sbin/sshd -D
