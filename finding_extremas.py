import numpy as np
import sympy as sym
from sympy import oo

'''
    Finding local and global maximumn and minimum of one time continuous functions
'''


def getCandidates(f,x):

    try:
        f_ = sym.Derivative(f,x)
        f1 = f_.doit()
        print('First derivative: %s'% f_.doit())

        roots = sym.solveset(f1,x)

        #print(roots)
        return roots
    except:
        print('Error happened, function may not be differentiable.')
        pass

def isExtrema_basic(num,f,x):
    try:
        delta = 0.1
        f_ = sym.Derivative(f,x)
        f1_lb = sym.lambdify(x,f_.doit())
        left = f1_lb(num-delta)
        right = f1_lb(num+delta)

        if (left > 0 and right < 0) or (left < 0 and right > 0):
            # must be an extrema
            retorno = True
        else:
            # undeterminated
            retorno = False
        
        return retorno

    except:
        print('Error happened :(')


def evaluate(num,f,x):
    try:
        if(abs(num) != oo):
            f_lb = sym.lambdify(x,f.doit())
            return f_lb(num)
        else:
            # we compute the limit instead
            return sym.limit(f,x,num)
    except:
        print('Error happened')

# function definition
x = sym.Symbol('x')
f = x**4 - 8 * x**2 + 356

candidate_points = []
candidate_points = list(getCandidates(f,x).args)
print(candidate_points)

sol = []
for n in candidate_points:
    if (isExtrema_basic(n,f,x)):
        sol.append(n)

# we add the two constraint boundaries of the function, that in this case are -inf and +inf
sol.append(oo)
sol.append(-oo)

pairs = {}
# now we evaluate the function f(x) for each of the values in sol, to obtain the value pairs (x,f(x))
for s in sol:
    pairs['%4.3f'% s] = evaluate(s,f,x)

print(pairs)
p1 = sym.plot(f)


