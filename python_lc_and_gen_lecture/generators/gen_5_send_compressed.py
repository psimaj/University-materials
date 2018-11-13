def natural_convolution():
    i = 0
    x = 1
    while True:
        x = yield i * x
        #yield yields the value first
        #and returns a value second
        i += 1

a = natural_convolution()
#the generator needs to be started before being sent anything
next(a)
#after calling next, the generator waits on the first yield
for i in range(1, 10):
    print(a.send(i))
    #the generator immediately yields the next value after receiving send
    #there's only one yield, so no need to call next
