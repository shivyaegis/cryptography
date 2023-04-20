import time

def space():
    print("\n\n")
    print("-"*50)
    print("\n\n")
    time.sleep(1)


def isPrime(n):
    # Corner cases
    if (n <= 1):
        return False
    if (n <= 3):
        return True
 
    # This is checked so that we can skip
    # middle five numbers in below loop
    if (n % 2 == 0 or n % 3 == 0):
        return False
    i = 5
    while(i * i <= n):
        if (n % i == 0 or n % (i + 2) == 0) :
            return False
        i = i + 6
 
    return True


def gcd(a,b):
    while b != 0:
        a, b = b, a % b
    return a


def primRoots(modulo):
    coprime_set = {num for num in range(1, modulo) if gcd(num, modulo) == 1}
    return [g for g in range(1, modulo) if coprime_set == {pow(g, powers, modulo)
            for powers in range(1, modulo)}]


def input_q():
    while True:
        q = int(input("Enter prime integer: "))
        if isPrime(q):
            print("Valid")
            space()
            break
        else:
            print("Invalid integer\n\n")
    return q


def input_x(q):
    while True:
        x = int(input("Enter X (X < q): "))
        if x >= q:
            print("Invalid\n\n")
        else:
            print("Valid")
            space()
            return x
        

def calculate_y(alpha,xa,q):
    y = (alpha**xa)%q
    print("Y is: ", y)
    space()
    return y


def secret_key(y,x,q):
    k = (y**x)%q
    print("Your secret key is: ", k)
    space()
    return k


space()
# prime number q
q = input_q()

# alpha primitive root of q and alpha < q
alpha = primRoots(q)
print("Primitive roots are:",alpha)
while True:
    choose = int(input("\nChoose primitve root index: "))
    if choose < len(alpha):
        if alpha[choose] < q:
            break
        else:
            print("Exceeds length of q\n")
    else:
        print("List index out of bounds\n")

print("Chosen primitive root is:", alpha[choose])
alpha = alpha[choose]
space()

# private Xa
print("Xa ->")
xa = input_x(q)

# private Xb
print("Xb ->")
xb = input_x(q)

# public Ya
print("Ya ->")
ya = calculate_y(alpha,xa,q)

# public Yb
print("Yb ->")
yb = calculate_y(alpha,xb,q)

# secret key of user A
print("secret key of user A")
key_a = secret_key(yb,xa,q)

# secret key of user B
print("secret key of user B")
key_b = secret_key(ya,xb,q)


# summarising
print("Summary: \n")
print("q -> ",q)
print("alpha -> ",alpha)
print("\nXa -> ",xa)
print("Xb -> ",xb)
print("\nYa -> ",ya)
print("Yb -> ",yb)
print("\nkey_a -> ",key_a)
print("key_b -> ",key_b)

space()