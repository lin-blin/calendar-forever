def prettify(res_f, c, m):
    weekday = ['воскресенье', 'понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота']
    print('День недели - {day}'.format(day=weekday[res_f]))

    ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    hunds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    thous = ["", "M", "MM", "MMM", "MMMM"]

    t = thous[c // 1000]
    h = hunds[c // 100 % 10]
    te = tens[c // 10 % 10]
    o = ones[c % 10]
    print('Век: ', t + h + te + o)

    month = {1: 'весна', 2: 'весна', 3: 'весна', 4: 'лето', 5: 'лето', 6: 'лето', 7: 'осень', 8: 'осень', 9: 'осень',
             10: 'зима', 11: 'зима', 12: 'зима'}
    print('Сезон: %s' % month[m])
