# print pattern

#                        *
#                       ***
#                      *****
#                     *******
#                    *********
#                   ***********   

n = int(input("Enter the height of tree: "))

a = 1
e = 1

while a < n:
    for c in range (0,n-a):
        print(" ",end=" ")
    for d in range (0,e):
        print("*",end=" ")
    print()
    e = e+2
    a = a+1