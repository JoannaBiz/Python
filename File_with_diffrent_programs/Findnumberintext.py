import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
print(phoneNumRegex.findall('Call me 123-123-1234 and 555-666-7777'))
