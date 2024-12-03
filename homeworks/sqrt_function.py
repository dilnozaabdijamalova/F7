### faqat int ildizini topadigan 1- usul
def sqrt_func ( num:int ):
    res = 0
    for i in range(1,num+1):
        res = num/i
        if i==res:
            res = int(res)
            break
        if i==num/2:
            res = " - butun son emas!"
            break
    return res
    

a = 169
res = sqrt_func(a)
# print(f" {a} soni kvadrat ildizi : {res}")

###   float ildizini topadigan 2- usul
def sqrt_func_dec ( num:int ):
    
    div = 1
    res1 = num/div

    while res1>=div:
        res1 = num/div
        if div==res1:
            break
        else: div += 0.01
       
    return "{:.2f}".format(res1)

b = 431
res1 = sqrt_func_dec(b)
print(f" {b} soni kvadrat ildizi = {res1}")




def sqrt_newton_method(A, tolerance=1e-10, max_iterations=1000):
    # Initial guess (You can also try with A / 2 for better initial guess)
    x = A / 2.0
    
    for _ in range(max_iterations):
        # Apply the Newton-Raphson formula
        x_next = 0.5 * (x + A / x)
        
        # Check for convergence
        if abs(x_next - x) < tolerance:
            return x_next
        
        # Update the guess
        x = x_next
    
    return x  # Return the result if we exceed max iterations

# Test the function
A = 431
print(f"Square root of {A} is approximately {sqrt_newton_method(A)}")
