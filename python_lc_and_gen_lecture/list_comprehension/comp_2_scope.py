a = [i for i in range(10)]
#name 'i' is not defined in the global scope
#referencing it shall produce an error
#print(i)

a = []
for i in range(10):
    a.append(i)

#name 'i' will be defined
#which makes the above statements NOT fully equivalent
print(i)

#the following also doesn't work
#the list is first fully evaluated
#and is only named 'b' after it's fully built
#b = [0 if i == 0 else b[i-1] for i in range(10)]
