# check if a number is palindrome

# Palindrome number is -> 123321 -> reverse number is same as the original
# 123321 reverse of this number is 123321

num = int(input("Enter a number to check whether palindrome or not"))

res = str(num) == str(num)[::-1]

print("Is the number palindrome ? : " + str(res))

# do it without converting to string