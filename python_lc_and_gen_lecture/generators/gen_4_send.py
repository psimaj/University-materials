def natural_convolution():
    i = 0
    x = 1
    while True:
        i += 1
        x = yield
        yield None if x is None else i*x

a = natural_convolution()
#the generator needs to be started before being sent anything
next(a)
#after calling next, the generator waits on the first yield
for i in range(1, 10):
    if i % 3 != 0:
        print(a.send(i))
        #the generator immediately yields the next value after receiving send
    else:
        print(next(a))
        #when a generator waits for a yield to return, calling next is
        #equivalent to calling send(None)
    next(a)
    #next sets the generator at the next yield
    #a yield which returns from next, and not send, returns a None value
