import csv
import pandas

FILE_PATH = '/python/100days/day25_intermediate_pandas/weather_data.csv'

# with open(FILE_PATH, 'r') as file:
#     for line in file:
#         print(line.strip())
        
# print()
# with open(FILE_PATH, 'r') as file:
#     data = csv.reader(file)
#     print(data)
#     for row in data:
#         print(row)
        
# print()
# with open(FILE_PATH, 'r') as file:
#     data = csv.reader(file)
#     temperature = []
#     for _,temp,_ in data:
#         if temp != 'temp': temperature.append(int(temp))
#     print(temperature)
    
data = pandas.read_csv(FILE_PATH)
print(data)
print(data['temp'].to_list())
print(data['temp'].mean())
print(data.temp.max())

print(data.where(data['day'] == 'Monday'))

print(data[data['day'] == 'Monday'])

print(data[data.temp == data.temp.max()])