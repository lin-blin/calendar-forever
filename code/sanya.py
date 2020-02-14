string = '30 октября 2019'
def get_data(string):
    data = string.split()
    d = int(data[0])
    m = 0
    y = int(data[2])
    c = y // 100 + 1
    return (d, m, y, c)
    #print(data)
print(get_data(string))