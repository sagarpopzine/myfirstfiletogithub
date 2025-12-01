tuple1=(12,6,-8,'jenny',True)
print(tuple1)

tuple1=(12,6,-8,'jenny',True)
print(tuple1[3])

tuple1=(12,6,-8,'jenny',True)
print(type(tuple1))

tuple1=(12,6,-8,'jenny',True)
tuple2=(45)
print(type(tuple2))

tuple1=(12,6,-8,'jenny',True)
tuple2=(45,)
print(type(tuple2))

tuple1=(12,6,-8,'jenny',True,12,6)
print(tuple1[:5])

tuple1=(12,6,-8,'jenny',True,12,6)
print(tuple1[::3])

tuple1=(12,6,-8,'jenny',True,12,6)
print(len(tuple1))

tuple1=(12,6,-8,'jenny',True,12,6)
tuple2=(45,56,47)
tuple3=(tuple1,tuple2)
print(tuple3)

tuple1=(12,6,-8,'jenny',True,12,6)
tuple2=(45,56,47)
tuple3=tuple1+tuple2
print(tuple3)

tuple1=(12,6,-8,'jenny',True,12,6)
print(tuple1.count(6))

tuple1=(12,6,-8,'jenny',True,12,6)
print(tuple1.index('jenny'))

list1=(1,2,3,4,5)
print(list(list1))