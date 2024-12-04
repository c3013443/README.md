from sympy import symbols, sin, diff, solve
from sympy import lambdify
import math

x = symbols('x')
f = sin(2*x) - (x**3 - 3*x**2 - 6*x + 7) # Define the variable and the equation


f_prime = diff(f, x)# gives the derivative of f(x)

f_lambdified = lambdify(x, f)
f_prime_lambdified = lambdify(x, f_prime)# Convert the symbolic expressions to functions for numerical evaluation



def newton_raphson(initial_guess, tolerance=1e-6, max_iterations=100):# Newton-Raphson method
    current_guess = initial_guess
    for iteration in range(max_iterations): #Range given and processed for iteration up to 100
        f_value = f_lambdified(current_guess)
        f_prime_value = f_prime_lambdified(current_guess)  # Evaluate function and derivative at current guess
        
        if f_prime_value == 0:
            print("Zero derivative encountered. No solution found.")# no return from no solution
            return None
        
        
        next_guess = current_guess - f_value / f_prime_value # Update prior findings using Newton-Raphson formula
        
        print(f"Iteration {iteration + 1}: x = {next_guess}, f(x) = {f_value}")
        
        # Check for convergence
        if abs(next_guess - current_guess) < tolerance:
            print(f"Converged to {next_guess} after {iteration + 1} iterations.")
            return next_guess
        
        current_guess = next_guess
    
    print("Maximum iterations reached. No solution found.") # no solution no return
    return None

# Example usage
initial_guess = 2.0  # Start
solution = newton_raphson(initial_guess)

if solution is not None:
    print(f"Approximate solution: {solution}")
