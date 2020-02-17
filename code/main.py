import datetime

# Тесты
test = ['29 февраля 2020', '1 июня 2015 ', '5 апреля 1242', '12 июня 1812', '24 октября 888']

# Данные
monthes = {'мар': 1, 'апр': 2, 'мая': 3, 'июн': 4, 'июл': 5, 'авг': 6, 'сен': 7, 'окт': 8, 'ноя': 9, 'дек': 10,
             'янв': 11, 'фев': 12}
days = ['воскресенье', 'понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота']

# Объявление функций
def get_data(string, monthes):
    '''Функция преобразовывает строку пользователся в набор числовых
    значений для дальнейшей работы с ними.

    :param string typed string:
    :param month typed dict:
    :return day, month, century, year typed tuple:

    '''

    data = string.split()
    d = int(data[0])
    m = monthes[data[1][0:3]]
    y = int(data[2]) % 100

    if m > 10:
        y -= 1

    if y == -1:
        y = 100

    c = int(data[2]) // 100
    return d, m, c, y

def get_answer(d, m, c, y):
    '''Функция вычисляет день недели по заданной пользователем дате.

    :param d typed int:
    :param m typed int:
    :param c typed int:
    :param y typed int:
    :return answer typed int (0-6):

    '''

    answer = (d + int((13 * m - 1) / 5) + y + int(y / 4) - 2 * c + int(c / 4)) % 7
    return answer

def prettify(weekday, *data):
    print('День недели - {day}'.format(day=weekday))

    ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    hunds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    thous = ["", "M", "MM", "MMM", "MMMM"]

    if data[3] != 100:
        century = data[2] + 1
    else:
        century = data[2]

    t = thous[century // 1000]
    h = hunds[century // 100 % 10]
    te = tens[century // 10 % 10]
    o = ones[century % 10]
    print('Век: {0}'.format(t + h + te + o))

    month = data[1]
    if month < 4:
        season = 'весна'
    elif month < 7:
        season = 'лето'
    elif month < 10:
        season = 'осень'
    else:
        season = 'зима'
    print('Сезон: {0}'.format(season))

    # Запись в TeX
    f = open('log.tex', 'w+')
    b = "\\documentclass{article}\n\\usepackage[cp1251]{inputenc}\n\\usepackage[russian]{babel}\n\n\\begin{document}"
    b += "\n" + "Введите дату >>>" + date + "\n" + "-" * 23 + "\n" + "День недели: " + weekday + "\n" + "Век: " + (
                t + h + te + o) + "\n" + "Сезон: " + season + "\n"
    b += "\n\\end{document}"
    f.write(b)
    f.close()

# Основная часть
date = input('Введите дату >>> ')
print('-' * 23)
data = get_data(date, monthes)
weekday = days[get_answer(*data)]
prettify(weekday, *data)

test_mod = False

# Тестовый модуль
if test_mod:
    data = date.split()
    d = int(data[0])
    m1 = monthes[data[1][0:3]]
    m = m1 - 10 if m1 > 10 else m1 + 2
    y = int(data[2])

    day_ = datetime.datetime(y, m, d)
    weekday_ = datetime.datetime.weekday(day_)

    if weekday_ < 6:
        weekday_ = weekday_ + 1
    else:
        weekday_ = 0

    weekday2 = days[weekday_]

    print('-' * 23)
    print('Проверка при помощи встроенного модуля:', weekday == weekday2)  # сравнение результатов