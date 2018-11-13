#printing a 0-valued n-dimension array
#every dimension of which is of size n
#restriction: one line
#don't do this in serious projects

print((lambda i: (lambda x: lambda y: x(x, y))(lambda self, z: [0] * i if z == 1 else [self(self, z-1) for i in range(i)])(i))(int(input())))
