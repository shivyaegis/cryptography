import time
import random

def space():
    print("\n")
    print("----".center(70,"-"))
    print("\n\n")
    time.sleep(2)


def print_factors(x):
    print("\n\nThe factors of",x,"are:")
    list1 = []
    for i in range(1, x + 1):
        if x % i == 0:
            list1.append(i)
    print(list1)
    return list1


def public_key(f):
    temp = 1
    for i in range(1,len(f)):
        if i not in f:
            temp = i
            break
    return temp
    

def private_key(e,ph):
    while True:
        # k = random.randrange(start=2,stop=20,step=1)
        k = 2
        d = (k*phi + 1) / e
        d = int(d)
        break
            # if (d*e)%ph == 1:
            #     break
            # else:
            #     continue
    return d


list1 = []
lower = 1
upper = int(input("\n\n\nEnter no of bits for RSA: (bits) "))
ones = int("1"*upper,2)
time.sleep(1)
print("\nUpper range for RSA (decimal) is: ",ones)
upper = ones

for i in range(lower,upper):
   for j in range(2, i):
      if(i % j == 0):
         break
   else:
      list1.append(i)

space()

print("Prime numbers in the range",lower,"to",upper,"are:",list1)
print("\nChoose prime numbers to use:")
choice1 = int(input(""))
choice2 = int(input(""))

prime1 = choice1
prime2 = choice2

n = prime1 * prime2
phi = (prime1-1) * (prime2-1)

space()
print("Prime number 1: ",prime1, "\nPrime number 2: ",prime2, "\n\nMultiplication result(n): ",n,"\nPhi(n) is: ",phi)

factors = print_factors(n)

time.sleep(1)
space()

e = public_key(factors)

print("We take E as: ",e)
time.sleep(1)

d = private_key(e,phi)
print("D is: ", d)

space()
print("Public key : {",e,",",n,"}")
print("Private key : {",d,",",n,"}")
space()

M = 6
cipher = (M**e)%n
plain = (cipher**d)%n

print("Cipher:",cipher,"\nPlain:",plain)
print("\n\n")

print("DONE".center(40,'_'))