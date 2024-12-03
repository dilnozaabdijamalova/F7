


# students = {"John":80,"Ann":85,"Alex":95,"Ahmed":100}

# letters = 'abcdefgh'

# numbers = [1,2,3,4,5,6,7,8,9]

# courses = [("Python",500),("SQL",400),("power BI",430)]


# leap_year = int(input('yearni kiriting   '))
# if (leap_year % 400 == 0) or (leap_year % 4 == 0 and leap_year % 100 != 0):
#     print('bu leap year')
# else:
#     print ('leap year emas')
    
    
# year = input('enter year ')
# year = int(year)

# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print('this year is leap year')
#         else: 
#             print('this year is not leap year')
#     else: 
#         print('this year is leap year')      
# else: 
#     print('this year is not leap year')



# letters = 'abcdefgh'

# letters_2 = ''

# for letter in letters:
#     letters_2  += letter.upper()


    
# numbers = [1,2,3,4,5,6,7,8,9]

# numbers2 = []
# for number in numbers:
#     numbers2.append(number**3)
    
# print(numbers2)
    
students = {"John":80,"Ann":85,"Alex":95,"Ahmed":100}


# for student,score in students.items():
#     print(f'{student}-{score}')

# print(tuple(students.items()))


# courses = [("Python",500),("SQL",400),("power BI",430)]

# for course, payment in courses:
#     print(course,payment)



# range 

# r1 = range(1,101)


# for i in range(2,101,2):
#     print(i)
   
# count = 0
# for number in range (1,101):
#     if number % 2 ==0:
#         count +=1
#         # print(number)
# print(f'We have {count} even numbers')


countries = ['USA','UK','Russia','Uzbekistan']

capitals = ['Washington','London','Moscow','Tashkent']

# for index,country in enumerate(countries):
#     print(f'Capital of {country} is {capitals[index]}')
    
# for index,letter in enumerate('abcdsejk'):
#     print(letter, ' - ', index)


# for capital,country in zip(capitals,countries):
#     print(f'Capital of {country} is {capital}')
    
    
# d2 = {}
# for capital,country in zip(capitals,countries):
#     d2[country] = capital
    
# print(d2)


# d2 = dict(zip(countries,capitals))
# print(d2)
# print(zip(countries,capitals))


# l2 = [[1,2,3],[4,5,6],[7,8,9]]

# l3 = []

# letters = 'abcdefgh'

# l4 = [i.upper() for i in letters if i !='d' and i !='a']
# print(l4)



# numbers = [j**2 for j in range(1,100,2)]

# print(numbers)

# a = 0
# while a <= 100:
#     if a ==56:
#         a = a + 1
#         continue
#     print(a)
#     a = a +1


ls = [('A', 5), ('A', -3), ('B', 2), ('C', 3), ('A', -2), ('C', -2)]

res = {'A': 0, 'B': 2, 'C': 1}


res = {}

for key, value in ls:
    if key in res:
        res[key] += value
    else:
        res[key] = value 
print(res)














    
    

