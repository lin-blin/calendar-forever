import math
#ФОРМУЛЫ
#res = (d + math.floor(13*m-1) +math.floor(5*y/4) + math.floor(-7*c/4)) %
string = '13 февраля 2019'
#string = '30 октября 2019'
#string = '2 марта 2008'

def get_data(string):
    month = {'мар': 1, 'апр': 2, 'мая': 3, 'июн': 4, 'июл': 5, 'авг': 6, 'сен': 7, 'окт': 8, 'ноя': 9, 'дек': 10,
             'янв': 11, 'фев': 12}
    data = string.split()
    d = int(data[0])
    m = month[data[1][0:3]]
    y = int(data[2]) % 100
    c = int(data[2]) // 100
    return (d, m, c, y)

data = get_data(string)
print(data)
d = 30
def get_answer(d, m, c, y):
    #answer = (d +  6 + y + math.floor(y/4) + math.floor(c/4) -2*c) % 7
    answer = (d + int((13*m-1)/5) +int(5*y/4) + int(-7*c/4)) % 7
    #answer = (d + math.floor((13*m-1)/5) + math.floor(5*y/4) + 5 - c) % 7
    return answer

res = get_answer(*data)
print(res)
