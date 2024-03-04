s = input()
print("palindrome" if s == "".join(reversed(s)) else "not palindrome")