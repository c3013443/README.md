from sympy import sin
import math # wont work without?
import sympy as sp

print("question3") 
def question3(a,b,c,d):
    x = sp.symbols('x') #good.   #x=sin.symbols does not work  #used import symy as sp for fix
    f = a * sp.sin(b * x) + c * sp.exp(d * x) #redo for right order
    f_at_5=f.subs(x, 5)
    third_derivative = sp.diff(f, x, 3) #check later half
    definite_integral = sp.integrate(f, (x, 2 * sp.pi, sp.sqrt(6))) #sp function is different in interaction
    return [f_at_5, third_derivative, definite_integral]# gives ferivatives and integrals
print(question3(2,3,4,5))
    
