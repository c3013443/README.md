from sympy import sin
import math    #NO CAPS

print("Question2")
def question2(x):
    if x == 7/3:
        raise ValueError(" You cannot use any value which results in a denominator of 0.")# so they dont divide by 0
    try:
        numerator = math.sqrt(x) + 3 * (x ** 5) #note that * are vague
        denominator = 3 * x - 7 # use space bars
        return numerator/denominator
    except ValueError:
        raise ValueError("For this question you cannot square root a negative number and therefore x must be positive") #B
print(question2(9))
#using x values for the function 
