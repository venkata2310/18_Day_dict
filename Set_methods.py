# f= {}
# print(f,type(f)) # {} <class 'dict'>

# z={1,2,23,43,'hello',"python@"}
# print(z,type(z)) # {1, 2, 23, 'hello', 43, 'python@'} <class 'set'>

# d={4,2,34,13}
# print(d[1]) # type error

# a={1,4,6}
# print(a,type(a))
# s=frozenset(a)
# print(s[3]) #TypeError: 'frozenset' object is not subscriptable

# a={1,2,3,4}
# b=5,6,7,8,9
# a.add(b)
# print(a)

# z={2,5,6,7}
# z.clear()
# print(z) #set()

# a={1,2,3,4} ; b={3,4,5,6} ; c={5,6,7,8,0} ; d={6,7,8,9,0}
# print(a.intersection(b))
# print(b.intersection(c))
# print(c.intersection(d))
# print(d.intersection(a))

# a={3,5,6,'hello'}
# b={3,7,5,'hi'}
# print(a.union(b))
# print(b.union(a))
# print(c.union(a)) # NameError

'''doubt 1'''
# a={1,2,3}
# b={4,5,6}
# q= a.update(b)
# print(q) #none

