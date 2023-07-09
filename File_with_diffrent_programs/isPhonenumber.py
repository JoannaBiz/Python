
def isPhonenumber(text): # 123-123-1234
    if len(text) != 12:
        return False
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4,7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8,12):
        if not text[i].isdecimal():
            return False
    return True

phone = ''
print("Write your phone number")
phone = input()

isPhonenumber(phone)

while isPhonenumber(phone) == False:
    print("It is not a phone number. Try again")
    phone = input()
else:
    print("It is a phone number.\n So I will call you tomorrow for your phone number:\n "+ str(phone))
