# adv. loop

# take a input from user as number and print reverse of no.

num = int(input("Enter a number: "))
rev = 0
while(num > 0):
    rem = num % 10
    rev = (rev * 10) + rem
    num = num // 10

print("\n Reverse of entered number is = %d" %rev)

# now try it with for loop
# try to decrease no. of lines, there is still scope of it.

