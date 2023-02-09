import pandas

FILE_PATH = 'D:\\python\\100days\\day25_intermediate_pandas\\2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv'
OUTPUT_PATH = 'D:\\python\\100days\\day25_intermediate_pandas\\Squirrel_Count.csv'

data = pandas.read_csv(FILE_PATH)

# print(data.columns)
# print(data['Primary Fur Color'])

fur_color_count = data[['Primary Fur Color']].groupby(['Primary Fur Color']).size()
data_dict = {
    "Fur color": fur_color_count.index,
    "Count": fur_color_count.values
}
fur_color = pandas.DataFrame(data_dict)
fur_color.to_csv(OUTPUT_PATH, index = False)