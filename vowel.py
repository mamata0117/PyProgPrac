# . Write a Python program to check whether a character entered by the user is a vowel or consonant.
#1

# char = input("Enter a character: ")

# if char in "aeiouAEIOU":
#     print(char, "is a vowel")
# else:
#     print(char, "is a consonant")
#2
char = input("Enter a character: ").lower()

if char in "aeiou":
    print(char, "is a vowel")
else:
    print(char, "is a consonant")    