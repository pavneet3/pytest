# input a number and print if a number is prime or not.

num = int(input("Enter a number: "))
if num > 1:
    for i in range(2,num):
        if(num % i == 0):
            print(num," is not a prime number")
            break
        else:
            print(num, "is a prime number")
            break

            