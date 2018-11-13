def big_powers(n):
    for i in range(n):
        yield i**i

print(big_powers(5))
#we print the generator object, not the values it yields

print(*big_powers(5))
#the * operator unpacks the values yielded by the generator
