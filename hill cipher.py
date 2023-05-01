import time
import copy

def space():
    # function to create space and make code clean
    print("\n\n")
    time.sleep(1)
    print("-".center(40,"-"))
    print("\n\n")


def create_mat(x, y):
    # creates a matrix with x rows and y columns
    temp = []
    t = []
    for i in range(x):
        
        for j in range(y):
            t.append(0)
        temp.append(copy.deepcopy(t))
        t = []
    return temp


def print_mat(txt, matrix):
    # prints a matrix
    print(txt + "\n")
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(str(matrix[i][j]).center(10," "),end="|")
        print("")
    space()


def add_to_matrix(data, matrix):
    # adds data to the matrix
    if len(data) == (len(matrix)*len(matrix[0])):
        count = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] = data[count]
                count += 1
    return matrix


def encrypt(pt, key):
    # encrypt data by multiplying pt and key and mod by 26
    result_mat = create_mat(3,1)
    list1 = []
    for i in range(3):
        cal = (pt[0][0]*key[0][i] + pt[1][0]*key[1][i] + pt[2][0]*key[2][i])%26
        list1.append(cal)

    result_mat = add_to_matrix(list1,result_mat)
    return result_mat


def plain_to_cipher(plain_text, key_mat):
    global alp

    # creating plain text matrix
    mat2 = create_mat(3,1)
    # print_mat("\nPlain text matrix",mat2)

    
    # converting pt to 3 letter blocks
    if len(plain_text)%3 != 0:
        plain_text = plain_text + "x"*(3-len(plain_text)%3)
    print("\n\n" + plain_text)

    # adding 3 letter blocks to encryption process
    ct = []
    for i in range(0,len(plain_text),3):
        mat2 = add_to_matrix([alp.index(plain_text[i]),alp.index(plain_text[i+1]),alp.index(plain_text[i+2])],mat2)
        # print(mat2)
        ct.append(encrypt(mat2, key_mat))

    space()
    # print_mat("CT matrix",ct)

    # conversion of ct int to alphabet
    cipher = ""
    for i in range(len(ct)):
        for j in range(len(ct[0])):
            cipher = cipher + alp[ct[i][j][0]]
            # print(cipher)

    return cipher


def main():
    global alp
    space()

    # creating key matrix
    mat1 = create_mat(3, 3)
    print_mat("Key matrix",mat1)

    # adding key to key matrix
    key = [17, 17, 5, 21, 18, 21, 2, 2, 19]
    mat1 = add_to_matrix(key,mat1)
    print_mat("Key matrix after key insertion:",mat1)

    # taking pt as input from user
    pt = str(input("Enter plain text:"))
    pt = pt.lower()
    
    plain = ""
    for i in pt:
        if i in alp:
            plain = plain + i

    ct = plain_to_cipher(plain, mat1)

    print("Cipher text: \n\n" + ct)


alp = ["a", "b", "c", "d", "e", "f", "g", "h", "i",
       "j", "k", "l", "m", "n", "o", "p", "q", "r",
       "s", "t", "u", "v", "w", "x", "y", "z"]
main()