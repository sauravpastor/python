# tupleinbuilt
#  my_tuple=(10,20,30,40,50)
# print(type(my_tuple))
# print(len(my_tuple))
# print(max(my_tuple))
# print(min(my_tuple))
# print(sum(my_tuple))


# inbuilt method

# print(my_tuple.count(10))
#  print(my_tuple.index(10))
#  print(tuple(my_tuple))

 x=(10,20,30,40,50)

 y=(10,20,40)

 a=list(x)
 b=list(y)

 a.extend(b)
 print(tuple(a))

 
