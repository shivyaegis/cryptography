# code contributed by Shivam Sharma
# 9th Feb 2023

import time 

# function to print matrix elements
def print_(mat):
    print("----" * 30)
    for i in range(len(mat)):
        print("|", end=" ")
        for j in range(len(mat[0])):
            print(mat[i][j], end=" | ")
        print("")
    print("----" * 30)

# get plain text and key

print("\n","----"*30)
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
time.sleep(1)
print("\n\nPlain text is: ", plain_text, " Key is: ", key)

""" make the reference matrix 
here first row is the plain text reference
and first column is the key reference
we use both these columns and find intersection
the intersecting element is the ciphered text
for the paticular plain text """

list1 = []
list2 = []
count = 0
for i in range(len(alp)+1):
    count = i-1
    for j in range(len(alp)+1):
        if i==0 and j==0:
            # first element is blank only
            list1.append(" ")
        elif i==0:
            # if first row then just append alphabets but since j is one
            # step ahead subtract 1
            list1.append(alp[j-1])
        elif j==0:
            # if j is 0 then append the alphabet for key row
            list1.append(alp[i-1])
        else:
            # else we append the alphabet but shift it each row
            list1.append(alp[count%26])
            count += 1

    # append to one row in list and clear second list
    list2.append(list1)
    list1 = []

time.sleep(1)
print_(list2)

cipher = ""
# get i row and j column values and that is location of our cipher text [i][j]
# append it to cipher and do for all values in plain text
for k in range(len(plain_text)):
    i = list2[0].index(plain_text[k])
    j = list2[0].index(key[k])
    cipher = cipher + list2[i][j]
time.sleep(1)
print("\n\nCiphered text is: ", cipher)

