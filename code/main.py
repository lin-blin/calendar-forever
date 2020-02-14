import math

string = '13 февраля 2020'
string = '30 октября 2019'
string = '16 февраля 2020'

def get_data(string):
    month = {'мар': 1, 'апр': 2, 'мая': 3, 'июн': 4, 'июл': 5, 'авг': 6, 'сен': 7, 'окт': 8, 'ноя': 9, 'дек': 10,
             'янв': 11, 'фев': 12}
    data = string.split()
    d = int(data[0])
    m = month[data[1][0:3]]
    y = int(data[2]) % 100
    if m > 10:
        y -= 1
    c = int(data[2]) // 100
    return d, m, c, y

data = get_data(string)
print(data)

def get_answer(d, m, c, y):
    answer = (d + int((13*m-1)/5) + y + int(y/4) -2*c + int(c/4) ) % 7
    return answer


res = get_answer(*data)

print(res)
