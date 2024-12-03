


# Dictionary

# dict1 = {'id':1,'name':'John','email':'shdeaf@gmail.com','age':25}
# int1 = 25
# str1 = 'ufwhfijwe'
# list1 = [1,23,12,78]
# tuple1 = ('a','b','f')

# details_niso = ['Niso',25,'B2']
# details_asror = [25,'B2','Asror']

# details_niso[1]
# details_asror[1]

# # print(dict1['email'])

# #1 -- key -- immutable -- (str,tuple)

# d2 = {"name":"John","age":14,"subjects":['math','English','History'],"relative":('Father,Mother,brother')}
# # print(d2)


# # print(d2['subjects'][2])
# d2['subjects'][2] = 'literature' 
# # print('literature')


# d2['courses'] = ['python','sql','power BI']

# print(d2['courses'])
# print(d2['courses'][1])
# d2['courses'][1] = 'math'
# print(d2['courses'][1])
# print(d2)

# dict1 = {'id':1,'name':'John','email':'shdeaf@gmail.com','age':25,"coursemate":{"id":2,"name":'Jack',"age":26}}

# # print(dict1['coursemate']['age'])

# dict1['city'] = 'Tashkent'



# dict1.update({"country":75})
# print(dict1.pop('city'))
# print(dict1)

 
#1 
# print(list(dict1.keys()))
# #2
# print(list(dict1.values()))
# #3
# print(list(dict1.items()))


# dict_l = [("id",2),("score",98),('behaviour','perfect')]

# l1 = [4,5,8,'gdjjfd']

# dict2 = dict(dict_l)
# print(dict2)



keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]


# {'Ten': 10, 'Twenty': 20, 'Thirty': 30}

# chars = ['a', kkk'b','c','d'] 


# dict1[3] = 'ijfiiwekfi'


res = {}
for i,val in enumerate(keys):
    print(i)
    print(val)
    res[val] = values[i]
    res["ten"] = values[0] 
     

print(res)











