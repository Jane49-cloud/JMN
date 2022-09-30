# tuples

tuple1 = (1, 2, 3, 4)
print(tuple1)

tuple2 = (1, 4, "mangoes", 'yellow')
print(tuple2)

# nested tuples

tuple3 = ('points', [1, 2, 3, 4], [8, 9, 10])
print(tuple3)

# tuples can be created without parenthesis (packing)
tuple4 = 101, 'American', 2000.00, "HR Department"
print(tuple4)

# slicing tuples
print(tuple4[1:-1])
# contination of tupples

one= ("welcome", 'to', 'this')
two =("course", "geek")
three = one + two
print(three)

# tuple builtin methods
print(max(tuple1))
print(min(tuple1))
print(len(tuple1))
print(sorted(tuple1))