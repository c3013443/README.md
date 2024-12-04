from sympy import sin # might not be required

print("Question 1")

def question1(n):
    if 1 <= n <= 100:           #Do not use caps at start of the words
        return (n + 1) % 6 == 0 #For adding 1 to any given number bfore dividing by 0
    else:
            raise ValueError("Input must be an integer between 1 and 100") # valueerror requires caps

print(question1(9))

# ValueError for anything outside a range printing with n=9 so id divises 10 by 6 and will print false

