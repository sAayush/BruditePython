starts_with = lambda instr, prefix: instr.startswith(prefix)

if __name__ == '__main__':
    instr = 'Hello World'
    prefix = 'H'
    print(starts_with(instr, prefix)) # Output: 'True