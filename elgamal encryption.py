import time
import random


def space():
    print("\n\n")
    print("-"*50)
    print("\n\n")
    time.sleep(1)


def gcd(a, b):
    if a < b:
        return gcd(b, a)
    elif a % b == 0:
        return b
    else:
        return gcd(b, a % b)


def get_a(q):
    i = 2
    while True:
        if gcd(i, q) == 1:
            break
        else:
            i += 1
    return i


def encrypt(s, text):
    encr = []
    for i in range(len(text)):
        encr.append((s*ord(text[i])))
    return encr


def decrypt(encr, s_):
    decr = ""
    for i in range(len(encr)):
        decr += (chr(encr[i]//s_))
    return decr


def main():

    # create key using Reciever A which gives us back public keys q,g,h and private key a
    q, g, h, a = A_create_key()

    # use q,g,h public key to create s which encrypts message at Sender B and we get key p and encrypted text
    p, encrypted = B(q, g, h)

    # send key p to Reciever A and private key a which belongs to Reciever A will decrypt the text 
    A(p, a, encrypted)


def A_create_key():
    # A side processes generating public and private keys
    print("A Side Process generating keys".center(50,"~"))

    # prime number chosen by A (public key)
    q = int(input("\nEnter a number: "))

    # random number g (public key)
    g = random.randint(2, q)
    print("g =", g)
    time.sleep(0.5)

    # random number a such that gcd(a,q) = 1
    # private key for A
    a = get_a(q)
    print("a =", a)
    time.sleep(0.5)

    # compute h (public key)
    h = g**a
    print("h =", h)
    time.sleep(0.5)
    space()

    return q, g, h, a


def A(p, a, encrypted):
    # A side processes
    print("A Side Process".center(50,"~"))

    s_ = p**a
    print("\ns' =", s_)
    time.sleep(0.5)
    decrytped = decrypt(encrypted, s_)
    print("\nDecrypted text is: ", decrytped)
    time.sleep(0.5)
    space()


def B(q, g, h):
    # B side processes
    print("B Side Process".center(50,"~"))

    # get k such that gcd(k,q) = 1
    k = get_a(q)
    print("\nk =", k)
    time.sleep(0.5)

    # compute p
    p = g**k
    print("p =", p)
    time.sleep(0.5)

    # compute s
    s = h**k
    print("s =", s)
    time.sleep(0.5)

    encrypted = encrypt(s, message)
    print("\n\nEncrypted Data is:",encrypted)
    time.sleep(0.5)
    space()
    return p, encrypted



space()
message = str(input("Enter message: "))
space()
main()


# elgamal encryption algorithm
# see https://www.geeksforgeeks.org/elgamal-encryption-algorithm/ for algorithm working
