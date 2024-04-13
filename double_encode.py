import binascii

while(True):
    text = input("Please enter the text you want to double encode : ")
    text = [*text]
    for letter in range(len(text)):
        text[letter] = "%25"+binascii.hexlify(text[letter].encode()).decode("utf-8")
    print(''.join(text))