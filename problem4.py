largest_palindrome = 0
for num1 in range(100, 1000):
    for num2 in range(num1, 1000):
        prod = num1 * num2
        s_num = str(prod)
        if s_num == s_num[::-1]:
            if prod > largest_palindrome:
                largest_palindrome = prod
print(largest_palindrome)
