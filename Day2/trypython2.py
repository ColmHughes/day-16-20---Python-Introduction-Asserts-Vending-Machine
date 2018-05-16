# l = []

# l.append('A')
# l.append('B')
# l.append('C')

# m = l.copy()

# l.append('D')

# print(l)
# # start here: end here

# a = {
#     'name': 'Ann',
#     'age': 53,
#     'nationality': 'Irish'
# }
# b = {
#     'name': 'Bob',
#     'age': 43,
#     'nationality': 'English'
# }
# c = {
#     'name': 'Carl',
#     'age': 33,
#     'nationality': 'American'
# }



# l = [a, b, c]



# l = list(range(1,7))
# print(l)
# print(sum(l))

# m = list(range(0,100))
# print(m)


# n = list(range(10,51,2))
# print(len(n))

# o = [[0], [0, 1], [0, 1, 2],[0, 1, 2, 3], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5, 6]]
# print(o[4][3])

# listcomprehension = [list(range(i+1)) for i in range(7)]

# print(listcomprehension)





# evens = []
# for i in range(0,11):
#     if i % 2 == 0:
#         evens.append(i)
# print(evens)


# # Alternative - List comprehension
# evens = [x for x in range(11) if x % 2 == 0]
# print(evens)


                                                                                                                                                                                

# atLeastTen = ["cow", "pig", "sheep", "hen", "duck", "chicken", "horse", "donkey", "turkey", "goose"]
# print(atLeastTen[0])
# print(atLeastTen[-1])
# print(atLeastTen[1:])
# print(atLeastTen[:-1])

# # Create a dictionary that represents a student. Each student has a name, an age,
# # a nationality, and a list of subjects.

# a = {
#     'name' : 'Frank',
#     'age' : 26,
#     'nationality' : 'Irish',
#     'subjects' : ["Science", "Business", "Maths"]
# }

# b = {
#     'name' : 'Joe',
#     'age' : 20,
#     'nationality' : 'English',
#     'subjects' : ["Science", "Business", "Maths"]
# }

# c = {
#     'name' : 'Frank',
#     'age' : 11,
#     'nationality' : 'German',
#     'subjects' : ["Science", "Business", "Maths"]
# }

# d = {
#     'name' : 'Liam',
#     'age' : 40,
#     'nationality' : 'Dutch',
#     'subjects' : ["French", "Woodwork", "Maths"]
# }

# people = [a, b, c, d]
# print(people)

# # students = {a, b, c, d}
# # print(students)
# list = ["Here", "are", "a", "few", "words", "to", "test"]
# new = {
    
# }
# for i in range(0,len(list)-1):
#     new[list[i]] = len(list[i])
# print(new)
    
# print(len('antidisestablishmentarianism'))
    


# l = [i == j for i in range(10) for j in range(10)]


# l = []
# for i in range(10):
#     for j in range(10):
#         l.append(i == j)

# l = [i == j for i in range(10) for j in range(10) for k in ["A", "B", True]]
# print(len(l))

k = [k for i in range(2) for j in range(2) for k in ["A", "B", True]]
print(k)


