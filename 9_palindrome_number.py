def palindrome(number):
    number = list(number)
    number2 = number[::-1]
    if number == number2:
        return True
    return False

print(palindrome("123454321"))
