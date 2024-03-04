def is_palindrome(string):
    return string == string[::-1]

string = "radar"
if is_palindrome(string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")