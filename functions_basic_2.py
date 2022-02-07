#1
def countdown(n):
    newlist = []
    while n >= 0:
        newlist.append(n)
        n = n - 1
    return newlist

#print(countdown(5))

#2
def print_and_return(a):
    print(a[0])
    return a[1]

#print(print_and_return([1,2]))

#3
def first_plus_length(a):
    return a[0] + len(a)

#print(first_plus_length([1,2,3,4,5]))

#4
def values_greater_than_second(a):
    if len(a) < 2:
        return False
    newlist = []
    for x in a:
        if x > a[1]:
            newlist.append(x)
    print(len(newlist))
    return newlist

#print(values_greater_than_second([5,2,3,2,1,4]))
#print(values_greater_than_second([3]))

#5
def length_and_value(size, values):
    newlist = []
    for x in range(size):
        newlist.append(values)
    return newlist

#print(length_and_value(4,7))
#print(length_and_value(6,2))
