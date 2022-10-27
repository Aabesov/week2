# my_list = [1, 4, 2, 6, 8]
# my_list.reverse()
# print(my_list)
# my_list.sort(reverse=True)
# print(my_list)

# my_str = input(" ")
# word = list(my_str)
# word_reverse = list(my_str)
# word_reverse.reverse()
# if word == word_reverse:
#     print("Polindrom")
# else:
#     print("Does not polindrom")


# my_list = [1, 4, 2, 5, 6, 8, 4, 3, 2]
# my_list.remove(4)
# my_list.pop(3)
# print(my_list)

# for
# lists = [1, 4, 2, "Arsen", 2.3]
# for i in lists:
#     print(lists)


# num = []
# alpha = []
# for i in "sadh78yhjbjg6":
#     if i.isdigit():
#         num.append(i)
#     elif i.isalpha():
#         alpha.append(i)
# print(num)
# print(alpha)

# number = []
# n = [23, 342, 564, 254, 765, 14, 56, 865, 33, 7, 300, 21, 763, 1265, 213, 34]
# for i in n:
#     if i % 3 == 0 and i % 2 == 0:
#         number.append(i)
# print(number)


# n = []
# for i in list(range(1, 1000)):
#     if i % 2 == 0:
#             n.append(i)
# print(n)

# for i in range(4):
#     print("*****")


# num = int(input(" "))
# for i in range(1, 11):
#     print(f' {num} * {i} = {i * num}')









# def multiply(a, b, answer):
#     pass
a = int(input(""))
b = int(input(" "))
answer = int(input(" "))
if a * b == answer:
    print("Верно!")
else:
    print(f'Неверно. Правильный ответ {a * b}!')