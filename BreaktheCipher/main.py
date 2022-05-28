cipher = input("Enter cipher Text :")


def decipher(cipher):
    print("Brute Forcing the Cipher...")
    plain = ""
    x = 1
    for key in range(0, 26):
        for i in cipher:
            if i.isalpha():
                a = ord(i) - key
                if i.isupper() and a < 65:
                    plain += chr(a + 26)
                elif i.islower() and a < 97:
                    plain += chr(a + 26)
                else:
                    plain += chr(a)
            else:
                plain += i

        print(x, ")Brute Forcing...\n ",cipher, " = ", plain)
        plain = ""
        x += 1

decipher(cipher)
