import numpy as np
from matplotlib import pyplot as plt

'''
    Newton's Method
        (1) Univariable optimization
            (1.1) First order to find root
            (1.2) Second order to find local minima
        (2) Multivariable optimization
'''
# (1)
#   Definitions
# Non convex but has a solution in interval [1,2]
def f(x):
    return float(x**3 + 2 * x**2 + 10*x - 20)
def df(x):
    return float(3 * x**2 + 4 * x + 10)
def d2f(x):
    return float(6 * x + 4)

# Convex in interval [0,1]
def g(x):
    return float(x**3 + 14 * x**2 - 12 * x + 2)
def dg(x):
    return float(3 * x**2 + 28*x-12)
def d2g(x):
    return float(6 * x + 28)

#   Prooving that f(x) has solution in the interval [1,2]
'''
    Intermediate Value Theorem: 
        Let f be a real-valued function, defined and continuous
        on a bounded closed interval [a, b] of the real line. Assume, further, that
        f(a)f(b) ≤ 0; then, there exists ξ in [a, b] such that f(ξ)=0.
'''
print('In the interval [1,2], f(1) = %d, and f(2) = %d, furthemore, f(1)f(2) ≤ 0 is %s' % (f(1),f(2),f(1)*f(2) <= 0))
'''
    Therefore 0 belongs to the open interval whose endpoints are f(a) and f(b). 
    By the Intermediate Value Theorem, there exists ξ in the open 
    interval (1,2) such that f(ξ) = 0.
'''
# (1.1)
# Univariable Newton's Method, first order approach:
def Newtons_Method_1st(f,df,x0,err,max_iter,debug):

    values = np.zeros(max_iter)
    xk = x0

    for n in range(0,max_iter):

        fxk = f(xk)
        dfxk = df(xk)

        if abs(fxk) < err:
            if debug: print('Solution found (', xk,') on iteration ',n, ' of Newtons Method')
            values[n:] = xk
            return xk, values
        if dfxk == 0:
            print('Error')
            return None
        values[n]=xk
        xk = xk - fxk/dfxk

        if debug: print('N', n+1, ': ',xk)

    print('Too many iterations')
    return None

# Example f(x)
print('Running Newtons Method using 1st order approach, for f(x), x_0 = 1, and 100 iterations:')
sol1, values1 = Newtons_Method_1st(f,df,1, 0.00000001, 100, True)

# (1.2)
def Netwons_Method_2nd(f,df,d2f,x0,err,max_iter,debug):
    
    values = np.zeros(max_iter)
    xk=x0

    for n in range(0,max_iter):

        fxk = f(xk)
        dfxk = df(xk)
        d2fxk = d2f(xk)

        if(abs(fxk) < err):
            if debug: print('Solution found (', xk,') on iteration ',n, ' of Newtons Method')
            values[n:] = xk
            return xk, values
        if d2fxk == 0:
            print('Error')
            return None
        
        values[n] = xk
        xk = xk - dfxk/d2fxk

        if debug: print('N',n+1, ': ', xk)

    print('Too many iterations')
    return xk, values

# Example f(x)
print()
print('Running Newtons Method using 2st order approach to find local minima in the non-convex function f(x), x_0 = 1, and 100 iterations:')
sol2, values2 = Netwons_Method_2nd(f,df,d2f,1, 0.00000001, 100, True)


# Plotting both approximations for f(x)
x_vect = np.array(range(100))
plt.plot(x_vect, values1,
        x_vect,values2)
plt.show()


# Example g(x)
print('Running Newtons Method using 1st order approach, for f(x), x_0 = 1, and 100 iterations:')
sol1, values1 = Newtons_Method_1st(g,dg,1.0, 0.00000001, 100, True)
# Finds closes root!!

# Example g(x)
print()
print('Running Newtons Method using 2st order approach, for f(x), x_0 = 1, and 100 iterations:')
sol2, values2 = Netwons_Method_2nd(g,dg,d2g,1.0, 0.000001, 100, True)
# Finds minimizer!


# Multivariate
H = np.array([[10,8],[8,10]])
print(H)