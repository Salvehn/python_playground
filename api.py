import requests

import zerorpc
apiKey = '27721ef0167e69d1708971dc196bf703'


class RPC(object):
    def weather(self, location):
        url = 'https://api.openweathermap.org/data/2.5/forecast?q={}&units=metric&appid={}'.format(location, apiKey)
        try:
            r = requests.get(url)
            return r.json()
        except requests.exceptions.RequestException as e:  # This is the correct syntax
            print('Caught Execption:', e)
        return None


s = zerorpc.Server(RPC())
s.bind("tcp://0.0.0.0:4242")
s.run()
