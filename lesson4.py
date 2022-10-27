# list_name = ["Aasasi", "zaswer", "sdasdsa"]
# i = len(list_name) - 1
# while i < len(list_name):
#     print(list_name[i])
#     if i == 0:
#         break
#     i -= 1

# tuple [list, tuple, set , dict]


# tuples= ([1,2,3], 4, 5)
# list, number, number2 = tuples
# print(list)
# print(number)
# print(number2)


# tuples= ([1,2,3], 4, 5)
# (list, *number) = tuples
# print(list)
# print(number)

# names = ("Nurlan", "Snamaly", "Nurlan", "Aman")
# print(names.count("Nurlan"))
# print(names.index("Nurlan"))

#
# tuples = ((), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d'))
# tuples = list(tuples)
# tuples_list = list()
# for i in tuples:
#     if type(i) == tuple and len(i) == 0:
#         continue
#     tuples_list.append(i)
# tuples = tuple(tuples_list)
# print(tuples)

#
# tuples = ((), ("a", "b"), 3, 5, (5,8,(),))
# tuples = list(tuples)
# tuples_list = list()
# tuples_list.append(tuples[1])
# print(tuples_list)

# def get_power(U, I):
#     return U * I
# result = get_power(4, 6)
# print(result)
#

# def find_max_and_min_digits(a, b, c):
#     return max(a, b, c)
# result = find_max_and_min_digits(12, 534, 2)
# print(result)

#

#
# def multiply(a, b, answer):
#     if answer == a * b:
#         return "Верно!"
#     else:
#         return "Неверно. Правильный ответ [a * b]!"
# result = multiply(4, 5, 21)
# print(result)
