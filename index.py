#GuidovanRossum<guido@python.org>

# писал в atom, так как pyCharm на macOs шалит(эффект залипания в редакторе)

import requests
from datetime import datetime


apiKey = '27721ef0167e69d1708971dc196bf703'


# JS array.prototype.every equivalent (ES6)
def every(list_, pred):
    return all(pred(i) for i in list_)


def decide():
    print(
        'Уточка, хочешь идти гулять?.'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()
    if options[option]:
        return True
    return False


def get_weather(api_key, location):
    url = 'https://api.openweathermap.org/data/2.5/forecast?q={}&units=metric&appid={}'.format(location, api_key)
    r = requests.get(url)
    return r.json()


def check():
    weather = get_weather(apiKey, 'moscow')
    list = weather['list']
    print('Уточка смотрит прогноз погоды...')
    check = {'Snow': False, 'Rain': False, 'Clouds': False}
    for x in list:
        temp = x['main']['temp_max']
        # -273
        print(''.join([
            str(datetime.fromtimestamp(x['dt'])),
            ' Temp: ',
            str(temp),
            'C',
            ' Погодные условия: ',
            x['weather'][0]['main']
            ])
        )
        conditions = x['weather'][0]['main']

        if conditions in check.keys():
            check[conditions] = True
    return check


def solution(a):
    # lambda func as JS arrow func equivalent
    if every(a.values(), lambda e: e == False):
        print('Сегодня будет хорошая погода!')
        return

    if a['Snow']:
        print('Уточке следует одеться теплее!')
    if a['Rain']:
        print('Уточке следует взять зонтик!')
    if a['Clouds']:
        print('Уточке следует знать, что сегодня будет пасмурно!')


dispatch = {
    'decide': decide,
    'check': check,
    'solution': solution
}


def sequence():
    prev = ''
    for k, v in enumerate(dispatch):
        if k == (len(dispatch)-1):
            dispatch[v](prev)
            return
        prev = dispatch[v]()


if __name__ == '__main__':
    sequence()
