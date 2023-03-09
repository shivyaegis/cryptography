import time

time.sleep(1)
print("Welcome".center(30,"-"))

# taking input of pt and shift key

pt = str(input("\n\nEnter your plain text: "))
key = int(input("\nEnter shift key: "))

# convert to normal standards

pt = pt.upper()
key = key % 26

# alphabet list

alp = ["A", "B", "C", "D", "E", "F", "G", "H", "I",
       "J", "K", "L", "M", "N", "O", "P", "Q", "R",
       "S", "T", "U", "V", "W", "X", "Y", "Z"]

ct = ""

# encipherment take blank space as it is
# and for rest do (pt + key)mod26
print("---"*20)

for i in pt:
    if i == " ":
        ct += " "
    else:
        index = alp.index(i)
        index = (index + key) % 26
        ct += alp[index]

time.sleep(1)
print("\n\nYour ciphered text is: ", ct)


time.sleep(1)

# for decipherment take space as it is
# then do (ct-key)mod26

pt = ""
for j in ct:
    if j == " ":
        pt += " "
    else:
        index = alp.index(j)
        index = (index - key) % 26
        pt += alp[index]

print("\n\nYour plain text is: ", pt) 