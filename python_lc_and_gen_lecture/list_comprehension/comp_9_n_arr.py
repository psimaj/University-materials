"""
in this example, we build and print an n-dimensional array every dimension of which is also size n in addition, we restrict ourselves to just one line

let's start from a multiline solution this kind of array can easily be defined recursively since looking at it from the outside, it's an n-element array each element of which is also an n-element array but of one fewer dimension

so we can create a simple recursive function using list comprehension
"""
#def n_arr(n, dim):
#    return [0] * n if dim == 1 else [n_arr(n, dim-1) for i in range(n)]

#n = 3
#print(n_arr(n, n))
"""
in order to reduce this solution to one line, let's convert n_arr into lambdas since n_arr is recursive and lambdas don't know their own name the function's name will have to be passed to it as an argument also assume than n is know globally
"""
#arr = lambda self, k: [0] * n if k == 1 else [self(self, k-1) for i in range(n)]
"""
but if we are restricted to one line, we can't spend one to name our function so we'll need an another lambda which takes a lambda as an argument and returns a lambda, which is the received lambda with first argument substituted by itself
"""
#sub = lambda x : lambda y : x(x, y)
"""
lastly notice that we can't afford to actually save n globally so we're going to need another lambda which takes the n as an argument and substitutes it in the body of arr so in the end, we arrive at the following solution:
"""
#total = lambda n : (lambda x : lambda y : x(x, y))(lambda self, k : [0] * n if k == 1 else [self(self, k-1) for i in range(n)])(n)

#print(total(3))
"""
which we can compose into just one line:
"""

print((lambda n : (lambda x : lambda y : x(x, y))(lambda self, k : [0] * n if k == 1 else [self(self, k-1) for i in range(n)])(n))(int(input())))

"""
don't do this in serious projects
"""
