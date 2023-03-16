from itertools import chain
import time

def alphabets():
    alpha = "abcdefghijklmnopqrstuvwxyz"
    list1 = []
    for i in alpha:
        list1.append(i)
    return list1


def matrix():
    list1 = []
    list2 = []
    for i in range(5):
        list1.append("0")
    for j in range(5):
        list2.append(list1.copy())
    return list2


def print_matrix(table):
    print(("----"*7).center(40,"-"))
    for i in range(len(table)):
        print("|", end=" ")
        for j in range(len(table)):
            print(table[i][j].center(3," "), end="  |  ")
            # time.sleep(0.2)
        print("")
        print(("----"*7).center(40,"-"))


def check(ch):
    for i in alp:
        if i not in ch:
            return i
    return "x"


def pair(plain):
    # checks which alphabets have been used
    used = []

    # gets paired plain text with extra alphabets (if any)
    paired = []

    # counter
    b = 0

    while b < len(plain):

        # if pointer is at end
        if b == len(plain) - 1:

            # append to used and choose unused alphabet and return
            used.append(plain[b])
            z = check(used)
            paired.append(plain[b] + z)
            used.append(z)

            b += 1

        else:

            # check if pairing letters are equal
            if plain[b] == plain[b + 1]:
                # add element + var and element 2 + var2 and increment 2

                used.append(plain[b])
                z = check(used)
                paired.append(plain[b] + z)
                used.append(z)

                used.append(plain[b + 1])
                z = check(used)
                paired.append(plain[b + 1] + z)
                used.append(z)

                b += 2

            else:
                # add two elements to paired and used and increment
                paired.append(plain[b] + plain[b + 1])

                used.append(plain[b])
                used.append(plain[b + 1])

                b += 2

    return paired


def intable(str1, tab):
    if {str1}.issubset(chain.from_iterable(tab)):
        return True
    else:
        return False


def fill_key(k, mesh):
    i = 0
    j = 0

    while i < len(mesh) and j < len(mesh) and k != "":

        # if i or j is detected then
        if k[0] == "i" or k[0] == "j":

            # if not in table
            if not intable("ij", mesh):
                mesh[i][j] = "ij"

            # if not in table keep pointer here only
            else:
                if j > 0:
                    j -= 1
                elif j == 0:
                    j -= 1
                else:
                    i -= 1
                    j = len(mesh)

        # for other elements
        else:
            # if they don't exist already
            if not intable(k[0], mesh):
                mesh[i][j] = k[0]

            # otherwise, keep pointer here
            else:
                if j > 0:
                    j -= 1
                elif j == 0:
                        j -= 1
                else:
                    i -= 1
                    j = len(mesh)

        k = k[1:]
        j += 1
        if j == len(mesh):
            i += 1
            j = 0

    print("Key matrix after filling key: ")
    print_matrix(mesh)
    print("\n\n")

    for letter in alp:
        if not intable(letter, mesh) and i < len(mesh) and j < len(mesh):

            # if i or j is detected then
            if letter == "i" or letter == "j":
                # if not in table
                if not intable("ij", mesh):
                    mesh[i][j] = "ij"

                # if not in table keep pointer here only
                else:
                    if j > 0:
                        j -= 1
                    elif j == 0:
                        j -= 1
                    else:
                        i -= 1
                        j = len(mesh)
            else:
                mesh[i][j] = letter
            j += 1
            if j == len(mesh):
                i += 1
                j = 0

    print("Key matrix after filling remaining spaces: ")
    print_matrix(mesh)
    return mesh


# def encrypt(pair_pl, pair_ke, mat):
    
#     # same row/column
#     # diff row/column
#     for i in pair_pl:
#         t1 = [(index1,index2) for index1,value1 in enumerate(mat) for index2,value2 in enumerate(value1) if value2==pair_pl[0][0]]
#         print(t1[0])
#     # t2 = [(index1,index2) for index1,value1 in enumerate(mat) for index2,value2 in enumerate(value1) if value2==plain[0]]


# defines alphabets
alp = alphabets()

# defines matrix
mat = matrix()

print("\n")
print("Welcome".center(50,"-"))

time.sleep(1)
print("\n\nPlayfair table generated as: ")

print_matrix(mat)

# take inputs
time.sleep(1)

pt = str(input("\n\n\nEnter plain text: "))
key = str(input("Enter key: "))

# convert to standard format
pt = pt.lower()
key = key.lower()

# get paired lists
time.sleep(1)
paired_list_pt = pair(pt)
paired_list_key = pair(key)

print("\n\n\nPaired pt: ", paired_list_pt)
print("\n\n\nPaired key: ", paired_list_key)

# fill key matrix with key and remaining alphabets
time.sleep(1)
print("\n\n")
key_mat = fill_key(key, mat)

# now we need to find ct
# encrypt(paired_list_pt, paired_list_key, key_mat)