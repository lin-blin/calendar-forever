# Тесты
test = []
month = {'мар': 1, 'апр': 2, 'мая': 3, 'июн': 4, 'июл': 5, 'авг': 6, 'сен': 7, 'окт': 8, 'ноя': 9, 'дек': 10,
             'янв': 11, 'фев': 12}
days = ['Воскресенье', 'Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота']

# Объявление функций
def get_data(string, month):
    '''Функция преобразовывает строку пользователся в набор числовых
    значений для дальнейшей работы с ними.

    :param string typed string:
    :param month typed dict:
    :return day, month, century, year typed tuple:

    '''

    data = string.split()
    d = int(data[0])
    m = month[data[1][0:3]]
    y = int(data[2]) % 100
    if m > 10:
        y -= 1
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

    answer = (d + int((13*m-1)/5) + y + int(y/4) -2*c + int(c/4) ) % 7
    return answer

def prettify():
    '''
    Функция форматного вывода
    '''
    pass

# Основная часть
message = '1) Продолжить \n2) Выход\n>>>'   # Пригласительное сообщение меню
choice = 1 # ПЦ
while choice != 2:

    date = input('Введите дату >>> ')
    print('-' * 23)
    data = get_data(date, month)
    res = get_answer(*data)
    print(days[res])
    #prettify()

    try:
        choice = int(input(message))
    except ValueError:
        print("Недопустимое значение.")
        choice = 1
