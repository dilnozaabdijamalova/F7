import requests

url = 'https://www.codey.uz/api/data'
respo = requests.get(url)
data1 = respo.json()
# print(data1)

with open ('employee_info.csv', 'w') as file:
    columns = ','.join(data1[0].keys())
    file.write(columns + '\n')
    for obj in data1:
        values = ','.join(map(str,obj.values()))
        file.write(values + '\n')



with open ('employee_info.csv', 'r') as f:
    content = f.read()
    print(content)
