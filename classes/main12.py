
# #Threading


# from threading import Thread
# import time

# def test(id:int):
#     print(f'Thread{id} is starting')
#     time.sleep(2)
#     print(f'thread{id} is finishing')
    
# th1 = Thread(target=test,args=(1,))


# print('main thread is started')
# threads : Thread = []
# for i in range(1,4):
#     th = Thread(target=test, args=(i,))
#     threads.append(th)
#     th.start()
# for j in threads:
#     j.join()
# print('main thread is finished')



# from concurrent.futures import ThreadPoolExecutor    

# print('main thread is started')
# with ThreadPoolExecutor(max_workers=3) as f:
#     f.map(test,range(3))
# print('main thread is finished')

result = {}
with open('sample.csv') as f:
    columns = f.readline().replace('\n','').split(',')
    for row in f:
        
        for index, column in enumerate(columns):
            if column in result.keys():
                result[column].append(row.replace('\n',',').split(',')[index])
            else:
                result[column] = []
print(result)

[(0,"id"),(1,"Name"),(2,"age")]

















# {"id":[1,2,3,4,5],
#  "name":['Alex','John'],
#  "Age":[25,26,28]}
# rezult = {}
# with open('sample.csv') as f:
#     columns = f.readline().replace('\n','').split(',')
#     for row in f:
#         for index, column in enumerate(columns):
#             if column in rezult.keys():
#                 rezult[column].append(row.replace('\n','').split(',')[index])
#             else:
#                 rezult[column] = []
#             # print(rezult.setdefault(column,[]))
#             # .append(row.replace('\n','').split(',')[index])
# print(rezult)
    
    

