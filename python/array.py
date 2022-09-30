# define and declare an array

array = [10, 20, 16, 18, 48, 64]
print(array)
print(array[0])
print(array[1])
print(array[2])
print(array[3])
# array.count()

colors = ['black', 'red', 'green', 'cyan', 'magenta', 'yellow']
print(colors)
print(colors[-1])
print(colors[-2])
colors.insert(2, 'white')
print(colors)
colors.remove('red')
print(colors)
colors.extend(array)
print(colors)
colors.pop(-3)
print(colors)

# multidimensional arrays
multid = (1, 2), (2, 4), (4, 6), (8, 4), (7, 8)
print(multid)
print(multid[0])
print(multid[0][-1])
