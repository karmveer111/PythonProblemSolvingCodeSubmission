#Problem set #2.1
#Name: Karmveer Kaur
#time: 6 hours

def evaluate_poly(poly, x):
    result = 0
    for i in poly:
        result += (poly[(poly.index(i))]) * (x ** (poly.index(i)))
    return result

##    equation=tuple(poly)
##    result=equation[0]
##    for i in range(1,len(equation)):
##        result += equation[i]*(x**i)
##        print(equation[i],result)
##        print(float(result))
poly = (0.0,0.0,5.0,9.3,7.0)
print(evaluate_poly(poly,-13))

 
#Problem set 2.2

def compute_deriv(poly):
    deriv = ()
    for i in poly:
        if (poly.index(i)) > 0:
            deriv = deriv + (((poly.index(i)) * i),)
    return deriv

##    equation = tuple(poly)
##    result = ()
##    result = result +(equation[1],)
##    for i in range(1,len(equation)):
##        if equation[i] != 0:
##            result += (equation[i]*i,)
##            print(result)
poly=(-13.39,0.0,17.5,3.0,1.0)
print(compute_deriv(poly))



    #Problem set 2.3
    

def compute_root(poly,x_0,epsilon):
    root = x_0
    i = 1.0
    deriv = compute_deriv(poly)
    
    while abs(evaluate_poly(poly, root)) > epsilon:
        root = root - evaluate_poly(poly, root) / evaluate_poly(deriv, root)
        i += 1.0
    return root, i

   ## root_poly = x_0
##    increment = 1
##    while (evaluate_poly(poly, root_poly))>= epsilon:
##        root_poly = (root_poly-evaluate_poly(poly, root_poly)/compute_deriv(poly,root_poly))
##        increment+=1
##    return [root_poly, increment]
poly = (-13.39, 0.0, 17.5, 3.0, 1.0)
x_0 = 0.1
epsilon = 0.0001
print(compute_root(poly, x_0, epsilon))
