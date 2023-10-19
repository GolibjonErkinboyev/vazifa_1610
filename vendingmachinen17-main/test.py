# a = list(i for i in range(10))
# print(a)
# res = []
# def add(n):
#     global res
#     return n + 1
# for i in a:
#     add(i)
# # print(res)
# # a = list(map(lambda x: x + 2, range(10)))
# # print(a)
# # from functools import reduce
# import random
# res = []
# for i in range(20):
#     res.append(random.randint(300, 1200))
#     # a = random.randint(18, 65)
# print(res)
# a = 'salom dunyodagilar'
# b = a.split(' ')
# print(b)
# a = reduce(lambda summa, x: summa + x, res)
# print(a, type(a))
# d = list(filter(lambda x:x > 40, res))
# print(d)
# a = 'olama'
# b = hash(a)
# print(b%7)

# a = {1,2,3,4}
# b = {3,4,5,6,7}
# a.difference_update(b)
# print(a)