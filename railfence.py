import copy
import time


def space():
    print("\n")
    print("----".center(20,"-"))
    time.sleep(1)


def matrix(rows, l, text):
    print("Your initial matrix is: ")
    list1 = []
    list2 = []

    for i in range(rows):
        for j in range(l):
            list2.append("b")
        list1.append(copy.deepcopy(list2))
        list2 = []

    return list1


def print_mat(m):
    for i in range(len(m)):
        for j in range(len(m[0])):
            print(m[i][j], end=" ")
        print("")


def add_pt(p, m):
    count = 0
    for i in range(len(m[0])):
        for j in range(len(m)):
            if count < len(p):
                m[j][i] = p[count]
            count += 1
    
    return m


def encrypt(m):
    cipher = ""
    for i in range(len(m)):
        for j in range(len(m[0])):
            cipher += m[i][j]
    return cipher


print("Welcome".center(50,"-"))

# take plain text input
pt = str(input("\n\nEnter plain text: "))
pt = pt.upper()

# take key as input it defines the number of rows
key = int(input("Enter key: "))

space()

# define the number of columns to have
if type(len(pt)/key) == float:
    i = len(pt)//key + 1 
else:
    i = len(pt)//key

# builds the initial matrix
rail = matrix(key, i, pt)
print_mat(rail)

space()
# add your pt to the matrix
rail = add_pt(pt, rail)
print("Matrix after adding plain text: ")
print_mat(rail)
space()

ct = encrypt(rail)
print("\nYour plain text was: ", pt)
print("Your cipher text is: ", ct)

space()

