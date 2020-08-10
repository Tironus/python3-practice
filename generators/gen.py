# Generators are used to store inifinte amounts of data in finite amounts of memory


def infinite_seq():
    num = 0
    while True:
        yield num
        num += 1
        yield "This is the second yield statement"


infinite = infinite_seq()

print(type(infinite))
print(next(infinite))
print(next(infinite))
print(next(infinite))
print(next(infinite))


# StopIteration error if list is finite, and generator reaches the end of the list

def finite_seq():
    num = [1,2,3]
    for n in num:
        yield n

finite = finite_seq()

print(type(finite))
print(next(finite)) # 1
print(next(finite)) # 2
print(next(finite)) # 3 END!
#print(next(finite)) # StopIteration


# Generator comprehensions use parenthesis instead of square brackets like list comprehensions

num_list = [1,2,3]
lc = [num**2 for num in num_list]
print(lc)

gc = (num**2 for num in num_list)
print(gc)