


# append
# insert
# extend
names = ['john','jack','ann']

# print(names)
# names[2] = 'sara'
# print(names)

# mutable , immutable

# mutable
    #1 -- list
# immutable 
    #1 string
    #2 tuple
# ordered
    #1 list
    #2 string
    #3 tuple

# unordered
    # set

# fname = 'John'
# lname = 'Dew'

# full_name = 'John 5' +  str(10)
# print(full_name)

# add_int = 5 + 5
# add_str = '5 ' + '5'

# print(add_int)
# print(type(add_str))
# # + str to str
# # * str to int


# msg = ['This', 'is','a', 'message']

# msg_str = ' '.join(msg)


# full_name = 'Ash,irov Hus,an'

# print(msg_str)
# a = full_name.split('/')


# print(a)


# shallowcopy, deepcopy

# import copy

# l1 =  [10, 20, 30, [1,2,3]]

# l1_copy = copy.deepcopy(l1)



# l1[3][2] = 60


# print(l1)
# print(l1_copy)


# tuple --

#immutable, iterable, orderdered

# tuple()

t2 = tuple('18')
# print(t2)

# second_way = (1,2,3)
# third_way = 1,2,3

# intg1 = (18,)

# print(type(second_way))
# print(type(third_way))
# print(type(intg1))

t3 = (1,2,3,5,6,7,8,3)


# print(t3.count(3))
# print(t3.index(3,-8))

num = '1456238'

# num = str(num)
# num = tuple(num)
# print(num)


# unpacking
l1 = ('Jahohir aka',25,'ehwufjewkfowe@gmail.com')

name,age,email = l1

details = ['Jahohir aka',25,'john','Tony','Tompson','ehwufjewkfowe@gmail.com']

name,age,*others,email = details

print(name)
print(age)
print(email)
print(others)









