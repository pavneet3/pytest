# Print pattern

#            *
#            ** 
#            ***
#            ****
#            *****
#            ******   

n = int(input("Enter the height of pyramid: "))
a = 0
while a < n:
        print("*"*a)
        a = a+1

# verify logic, it does not print pyramid of correct height, check on input as 5        

# justify why you used while, why not for.
