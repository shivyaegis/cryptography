import copy
import time
import random
from itertools import chain

# watch as I try to do DES 

def space():
    print("\n")
    print("----".center(70,"-"))
    time.sleep(0.5)


def print_mat_linear(m):
    for i in range(len(m)):
        print(m[i].ljust(9," "),end="")
        print("  ", end="")


def print_mat_2d(m):
    count = 0
    for i in range(len(m)):
        count += 1
        print("Block", count, end=": ")
        for j in range(len(m[0])):
            print(m[i][j].center(5," "),end=" ")
        print("")


def blocks(m, l):
    block = []
    temp = []
    count = 0
    # for the range of length of binary list

    for i in range(len(m)+l):

        if count < len(m):

            # if count is less then check mod not 0 and add to temp list
            if count%8 != 0 or count == 0:
                temp.append(m[i])
            else:

            # else append to block and clear temp
                block.append(copy.deepcopy(temp))
                temp = []
                temp.append(m[i])
        else:

            # if count more than length means we are adding padding bits

            if count%8 != 0 or count == 0:
                # if mod8 not 0 then append to temp
                temp.append(bin(0))

            else:
                # otherwise we append to block and clear temp
                block.append(copy.deepcopy(temp))
                temp = []
                temp.append(bin(0))

        count += 1
    
    # just for safety check if temp is not empty 
    # then add this to the block (idk about this part)
    if temp != []:
        block.append(copy.deepcopy(temp))

    return block


def key_gen():
    k = []
    for i in range(4):
        temp = random.randint(0,255)
        k.append(bin(temp))

    return k


def split(list1):

    left_block = []
    right_block = []
    for i in range(0,len(list1[0])-4):
        left_block.append(list1[0][i])
        right_block.append(list1[0][i+4])
    list1.remove(list1[0])

    print("\nYour left block is: \n")
    print_mat_linear(left_block)
    space()
    print("\nYour right block is: \n")
    print_mat_linear(right_block)
    space()
    return left_block,right_block

def F_fun(left_block,right_block,key):
    # Function F is defined over here
    xor = []
    for i in range(len(left_block)):
        xor.append(str(bin((int(right_block[i],2)^int(key[i],2)))))

    return xor


def xor(left_block,right_block,F):
    # XOR F and Left block and make this the right block
    right_block2 = []
    for i in range(len(left_block)):
        right_block2.append(str(bin((int(left_block[i],2)^int(F[i],2)))))

    # Make left as right
    left_block2 = right_block

    print("\nAfter\t XOR with left\t and shifting")
    print("\nYour left block is: \n")
    print_mat_linear(left_block2)
    print("\n\nYour right block is: \n")
    print_mat_linear(right_block2)
    space()

    return left_block2, right_block2

def start():
    global cipher
    # welcome message
    print("\n\n")
    print("Welcome".center(50,"-"))

    # take input of plain text
    # pt = "Hello World!"
    pt = str(input("\n\nEnter plain text: "))
    space()

    # converts plain text to binary and adds to binary list
    in_bin = []
    print("\nPlain text in binary: \n")
    for i in pt:
        in_bin.append(bin(ord(i)))
        
    print_mat_linear(in_bin)
    space()

    # see how many padding bits we need with r
    r = 8 - len(in_bin)%8
    # print("remainder: ", r)

    # make blocks of 64 bits with padding bits
    print("\nBinary blocks are: \n")
    b = blocks(in_bin, r)
    print_mat_2d(b)
    space()

    # here we need while loop for blocks of texts

    cipher = []

    count = 1
    while(b!=[]):
        print("\n\n\n\nFor Block number ", count, " The process is as follows: ")

        time.sleep(2)
        count += 1
        temp = []
        # initializing left and right block from plain text block

        left_block, right_block = split(b)

        # need to fix this
        for i in range(15):
            print('\n\n\n\n')
            # take random numbers from 0 to 255, convert them to binary and get 64 bit key
            key = key_gen()
            print("\n\n\n\nYour key ", i, " is: \n")
            print_mat_linear(key)
            space()

            F = F_fun(left_block,right_block,key)

            print("\nAfter \tXOR function\t - F - : \n")
            print_mat_linear(F)
            space()

            left_block, right_block = xor(left_block,right_block,F)

            if i < 5:
                time.sleep(2)
            elif i < 8:
                time.sleep(0.5)

        
        # now we swap left and right as final step and join them
        # this gives us the cipher text that is required

        for i in range(len(left_block)):
            temp.append(left_block[i])
            temp.append(right_block[i])

        cipher.append(temp)
        print("\n\n\n\nCipher block now is: \n")
        print_mat_2d(cipher)
        space()
        time.sleep(2)

            


start()

# ciphered = ""

# print(cipher)
# print(cipher[0][0])
# print(chr(int(cipher[0][0],2)))

# for i in cipher:
#     for j in cipher:
#         ciphered += chr(int(i,2))
        
# print("Cipher text is: ",ciphered)
# space()