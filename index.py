# GuidovanRossum<guido@python.org>
# последовательность этапов
# (на одном из этапов смотрит погоду на openweathermap API)
# писал в atom (с linter), так как pyCharm на macOs шалит(эффект залипания в редакторе)

import proto
from datetime import datetime
import zerorpc
from time import time

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


def get_weather():
    start = time()
    c = zerorpc.Client()
    c.connect("tcp://127.0.0.1:4242")
    weather = c.weather("moscow")
    end = time() - start
    print('API Response time : {}'.format(end))
    return weather


def check():
    weather = get_weather()
    list = weather['list']
    print('Уточка смотрит прогноз погоды...')
    check = {'Snow': False, 'Rain': False, 'Clouds': False}
    # print(proto.filter(1234, lambda x: x['weather'][0]['main'] == 'Snow'))
    for x in list:
        temp = x['main']['temp_max']
        # -273
        interval = proto.concat(*[
                ' ',
                str(datetime.fromtimestamp(x['dt'])),
                'Temp:',
                str(temp),
                'C',
                'Погодные условия:',
                x['weather'][0]['main']
            ]
        )

        print(interval)
        conditions = x['weather'][0]['main']

        if conditions in check.keys():
            check[conditions] = True
    return check


def solution(a):
    # lambda func as JS arrow func equivalent
    # every(a.values(), lambda e: e == False)
    # every(a.values(), lambda e: not True)
    if proto.every(a.values(), lambda e: e is False):
        print('Сегодня будет хорошая погода!')
        return

    if a['Snow']:
        print('Уточке следует одеться теплее!')
    if a['Clouds']:
        print('Уточке следует знать, что сегодня будет пасмурно!')
    if a['Rain']:
        print('Уточке следует взять зонтик!')
        print(
            'Уточка, взяла зонтик?.'
        )
        option = ''
        options = {'да': True, 'нет': False}
        while option not in options:
            print('Выберите: {}/{}'.format(*options))
            option = input()
        if options[option]:
            print('Уточка молодец)')
        print('Глупая уточка)')
    return


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
        if prev is None:
            break


if __name__ == '__main__':
    print('Client started')
    sequence()
