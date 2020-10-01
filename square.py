square = lambda number : number * number

n = 10
print('Squares of numbers from 1 to %d are:' % (n - 1))
for i in range(1, 10):
    print(square(i))
