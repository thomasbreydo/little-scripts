from string import ascii_lowercase as al
from termcolor import cprint
a = 0
print()
for i, c in enumerate(al):
    if a > 25:
        print(' '*8, end='')
    else:
        cprint(al[a:a+5].ljust(5).upper(), 'white', 'on_blue', end=' | ')
        a += 5
    cprint(c.upper(),'white', end=':')
    cprint(f"{i: 2}" if i <= 13 else i - 26,'white')
print()
