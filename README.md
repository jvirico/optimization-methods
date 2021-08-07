# Optimization Methods and related Calculus exercices
Review and coding practice with classic approximation and optimization methods, root computation, derivatives, limits computation using python and symbolic library sympy.

### Finding extremas of a function
1. Finding collection of extremas in a one time differentiable function using sympy. [finding_extremas](./finding_extremas.py)

### Newton's Method
1. First-order approximation to find closest root, context must satisfy Intermediate Value Theorem.
   1. Works for f(x) and g(x) since both have solutions near initialization point x0.
2. Optimization method that involve second-order approximations of the objective function using 1st and 2nd derivaties for univariable problems, and gradient and Hessian for multivariable problems.
   1. Univariable problems: doesn't work for f(x) since it is a non-convex function, works for g(x) that is convex in interval [0,1].


