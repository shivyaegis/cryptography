# code contributed by Shivam Sharma
# 9th Feb 2023

print("\n","----"*10)
plain_text = str(input("\nEnter plain text: "))
key = str(input("Enter key: "))

alp = ["A", "B", "C", "D", "E", "F", "G", "H", "I",
       "J", "K", "L", "M", "N", "O", "P", "Q", "R",
       "S", "T", "U", "V", "W", "X", "Y", "Z"]

# if key is smaller than plain text
while len(plain_text) > len(key):
    key = key + key

# to make key equal to plain text
key = key[0:len(plain_text)]
plain_text = plain_text.upper()
key = key.upper()
print("\nPlain text is: ", plain_text, " Key is: ", key, "\n")

# setting ciphered text to blank 
cipher = ""
fl = []
for i in range(len(plain_text)):

    # get index of plain text and key element
    # at ith position from alphabet list
    p_b = alp.index(plain_text[i])
    k_b = alp.index(key[i])

    # get cipher alphabet by xoring plain text and key 
    # values and modding with 26
    cipher = cipher + alp[(p_b^k_b)%26]

    # check if XOR was >= 26 then put the mod value in flag
    if p_b^k_b >= 26:
        fl.append(p_b^k_b)
    else:
        fl.append(0)


print("Encrypted text is: ", cipher)

# set decrypted text to blank 
decr = ""

for l in range(len(cipher)):
    # check if XOR was < 26 then use cipher text value
    if fl[l] == 0:
        c_b = alp.index(cipher[l])
    else:
        # use the value of actual XOR from flag list
        c_b = fl[l]
    k_b = alp.index(key[l])

    decr = decr + alp[(c_b^k_b)%26]

print("Decrypted text is: ", decr)
print("\n","----"*10)
