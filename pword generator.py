import string
import random
from time import sleep


def all_char(password):
    characters = string.ascii_letters + string.punctuation  + string.digits
    password ="".join(random.sample(characters,length))
    return password

def alpha(al):
    alphab = string.ascii_letters
    al = "".join(random.sample(alphab,length))
    return al

def spe_char(specials):
    special = string.punctuation
    specials = "".join(random.sample(special, length))
    return specials
def num(NUM):
    dig = string.digits
    NUM = "".join(random.sample(dig,length))
    return NUM

def al_nu(an):
    AN = string.ascii_letters + string.digits
    an = "".join((random.sample(AN,length)))
    return an

def nu_sp(ns):
    NS = string.punctuation + string.digits
    ns = "".join(random.sample(NS, length))
    return ns

def al_sp(aS):
    AS = string.ascii_letters + string.punctuation
    aS = "".join(random.sample(AS, length))
    return aS


print("                         Good evening!                       ")
print("           ....Welcome to the Password Generator.....        ")
print("What Type Of Password would you like?: ")
print("1. All Char Generator")
print("2. Only Alphabets Generator")
print("3. Only Special Character  Generator")
print("4. Only Numeric Character Generator")
print("5. Alphabets and Numeric Generator")
print("6. Numeric and Special Character Generator")
print("7. Alphabets and Special Character Generator",end="\n\n")

while True:

    choice = int(input("Enter  your choice: "))

    if choice==1:
        length = int(input("Enter The Number Of Characters You want to Generate: "))
        sleep(1)
        print("Please wait while your password is being processed.....",end="\n")
        sleep(2)
        print(all_char(length))
        break
    elif choice==2:
        length = int(input("Enter The Number Of Characters You want to Generate: "))
        sleep(1)
        print("Please wait while your password is being processed.....",end="\n")
        sleep(2)
        print(alpha(length))
        break
    elif choice==3:
        length = int(input("Enter The Number Of Characters You want to Generate: "))
        sleep(1)
        print("Please wait while your password is being processed.....",end="\n")
        sleep(2)
        print(spe_char(length))
        break
    elif choice==4:
        length = int(input("Enter The Number Of Characters You want to Generate: "))
        sleep(1)
        print("Please wait while your password is being processed.....",end="\n\n")
        sleep(2)
        print(num(length))
        break
    elif choice==5:
        length = int(input("Enter The Number Of Characters You want to Generate: "))
        sleep(1)
        print("Please wait while your password is being processed....." ,end="\n\n")
        sleep(2)
        print(al_nu(length))
        break
    elif choice==6:
        length = int(input("Enter The Number Of Characters You want to Generate: "))
        sleep(1)
        print("Please wait while your password is being processed....." ,end="\n\n")
        sleep(2)
        print(nu_sp(length))
        break
    elif choice==7:
        length = int(input("Enter The Number Of Characters You want to Generate: "))
        sleep(1)
        print("Please wait while your password is being processed.....",end="\n\n")
        sleep(2)
        print(al_sp(length))
        break
    else:
        print("You Have Enter Invalid Choice:", end="\n\n")
        sleep(3)
