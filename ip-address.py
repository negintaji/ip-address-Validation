#https://github.com/negintaji/ip-address-Validation.git

import re

ip = input()
number = r'(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])'

pattern = rf'{number}(\.{number}){{3}}'

if re.fullmatch(pattern, ip):
    print("Valid IP")
else:
    print("Invalid IP")
