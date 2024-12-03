#1 input 

# msg = 'My name is '

# a = 6 
# b = 5 


# a = int(input('Please enter first number '))
# b = int(input('Please enter second number '))

# p = 2 * (a+b)
# print('output is:', p)

#1 format
#2 

# name = input('Please enter your name ')
# age =int(input('Please enter your age '))
# group = input('please enter your group')

# msg = 'My name is {1} and i am {0} years old'.format(age,name)
# msg2 = f'My name is {name} from {group} and i am {age + 5}  years old'


# print(msg2)

# method, Function
#name = 'Husan'
#name1 = 28
# print(len(name))
# print(len(name1))
# print(type(name))
# print(type(name1))
# print(id(name))
# print(id(name1))


# print(name.upper())
# print(name.endswith('m'))
# print(name.upper())
# print(name.upper())

# if name.endswith('m'):
#     print('You are given 1000 $, you can get by arriving early') 
# else:
#     print('sorry')
# name = 'Husan'
# print(id(name))
# print(id(name.replace('u','u')))
# print(dir(name))

#l1 = [1,2,3,4,5,6,7,8,'Husan','Abdulloh',54.2,('a','b','c')]
# print(l1)
# print(id(l1))
# l1[9] = 'Javohir aka'
# print(l1)
# print(id(l1))

#names = ['Abdusattor aka','Niso','Abdulloh aka']

# pandas # dataframe, serries == series=column, dataframe = table 

# names.append('Javohir aka')
# print(names)
# names.append('Javohir aka')
# print(names)
#names = ['Abdusattor aka','Niso','Abdulloh aka']
# l2 = ['Husan',54,96,'Saidbek']
# print(len(names))
# names.append(l2)
# print(len(names))

# print(len(names))
# names.extend(l2)
# print(len(names))
# print(names)

# names.insert(0,'Suhrob aka')
# print(names)

# l = [15,42,68]


# names.remove('Suhrob aka')
# print(names)

c = 1
while(c!='e'):
    year = int(input("Please enter a year: "))
    if(year%4==0):
        if((year%100==0) & (year%400!=0)):
            print('not leap year')
        else:
            print('leap year')
    else :
        print('not leap yearr')
        
    print("\nto continue press any bottom, to exit press e ")
    c=input()















