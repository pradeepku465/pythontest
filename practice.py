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

