a = [i for i in range(10) if i % 2 == 0]
print(a)

#you can add multiple ifs
#which shall translate to their conjunction

a = [i for i in range(30) if i % 2 == 0 if i % 3 == 0]
print(a)
