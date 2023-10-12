OriginalText = "MyPlainText"
KEY = "ABC"

print ("Here is the original Text")
print (OriginalText)

print("Here is the Key Repeated up to the length of the original text")
for position, letter in enumerate(OriginalText):
	x = KEY[position % len(KEY)]
	print(x,end='')

print()

Encrypted_Values = []

for position, letter in enumerate(OriginalText):
	Letter_In_Key = KEY[position % len(KEY)]
	encrypted_byte = ord(letter) ^ ord(Letter_In_Key)
	Encrypted_Values.append(encrypted_byte)

print ("Here is the Encrypted Decimal")
print (Encrypted_Values)

print("Here is the encrypted Hex with the 0x preceding each value")
for i in Encrypted_Values:
	print(hex(i)+" ", end="")
print ()

print("Here is the encrypted HEX without the 0x preceding each value")
for i in Encrypted_Values:
	print(format(i, "x")+" ", end="")
