import sympy as sp # newton raphson is to be used

print("Section B Question 1")
def newton_raphson(eq, var, initial_guess, tol=1e-6, max_iter=100):   #Note all different parts are required for full functionality of newton raphson method
    f_prime = sp.diff(eq, var) # For the variables in the equation
    x_n = initial_guess   #Needed for later end product
    for _ in range (max_iter):
        f_val = eq.subs(var, x_n).evalf()
        f_prime_val = f_prime.subs(var, x_n).evalf() # range For maximum in the raphson method
        if f_prime_val == 0:
            raise ZeroDivisionError("The Newton raphson method requires a derivative that does not = 0. Please submit a different value.") # paramitors and limitations needed
        x_next = x_n - f_val / f_prime_val
        if abs(x_next - x_n) < tol:  # _ act inconsistent
            return x_next
        x_n = x_next
        raise ValueError("The newton raphson method in this case has not converged to a reasonable degree")# needed incase it doesnt converge
    x = sp.symbols('x')
    eq = sp.sin(2*x) - (x**3 - 3*x**2 - 6*x +7) # function 
    initial_guess = 2
    root = newton_raphson(eq, x, initial_guess)
    print(f"Root found: {root}")# no responding answer# Read question 2 
