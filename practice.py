import datetime

print ("Twinkle, twinkle, little star", "\n", "How I wonder what you are! Up above the world so high", "\n", "Like a diamond in the sky. Twinkle, twinkle, little star, "
                                                                                                             "How I wonder what you are")

print(datetime.datetime.now())

def area(b):
    area_circle= b*b
    #print(area_circle)
    return area_circle

print(area(2))

#reverse name
def reverse(firstname, lastname):
    lastnames=""
    firstnames=""
    lastnames=firstname
    firstnames=lastname
    print(firstnames, " ", lastnames)

reverse("mike", "tyson")

def tuplee(a,b,c,d):
    list=[a,b,c,d]
    tupll=(a,b,c,d)
    return list, tupll

print(tuplee(1,2,3,4))
colorlist=["Red", "Green", "white", "black"]
def color_list():
    global colorlist
    for a in reversed(colorlist):
        return a


color_list()

my_list=["Red", "Green", "white", "black"]
for i in range(len(my_list)):
    my_list
    reversed_list=[]
    reversed_list.append(my_list[i])
    # Print the reversed list

print("Reversed list:", reversed_list)


def cals(a):
    sum=0
    sum= (a+a*a+a*a*a)
    return sum


print(cals(5))

def mis(a):
    sum1=a
    sum2=a*a
    sum3=a*a*a
    sum_f=sum1+sum2+sum3
    return sum_f

print(mis(5))

#calculate volume
def volume(z):
    volume=z*z*z
    return volume

print(volume(2))
#starrtfr

#Write a Python program to test whether a number is within 100 of 1000 or 2000.

def within(b):
    if b<=100:
        print("number is less than 100")
    elif b >=100>=2000:
        print("number is less than 1000")
    else:
        print("number is above 1000")

within(3000)

#Write a Python program to calculate the sum of three given numbers. If the values are equal, return three times their sum.

def sum(a,b,c):
    if a==b==c:
        sum1=3*a
        return sum1
    else:
        sum2= (a+b+c)
        return sum2

#print(sum(1,2,3))

print(sum(1,1,1))

#Write a Python program that determines whether a given number (accepted from the user) is even or odd, and prints an appropriate message to the user.

def odd_even(b):
    mod = b % 2
    if mod > 0:

        print("number is odd")
    else:
        print("number is prime")

odd_even(4)

#match here the value is compared in each case:

def match_cases(b):
    match b:
        case 1:print("this is from case 1")
        case 2:(print("this is from case 2"))
        case _:print("no value")

match_cases(2)
#match here the value is compared in each case:
def day(c):
    match c:
        case 1: print("today sunday")
        case 2: print("today monday")
        case _: print("weekend")
day(3)
