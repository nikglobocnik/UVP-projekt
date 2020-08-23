import json
from obdelaj_stran import ustvari_json

currencies = dict()
history = []

with open('zajeta_stran.json', 'r', encoding='utf-8') as f:
    for l in json.load(f):
        curr = l.get('okrajsava')
        v = l.get('valuta')
        rate = l.get('tecaj')
        currencies.update({curr :(v,rate)})


class Convert:

    def __init__(self,value:float,curr1:str,curr2:str):
        self.value = value
        self.curr1 = curr1
        self.curr2 = curr2

    def converted(self):
        rate1 = 1/currencies.get(self.curr1)[1]
        rate2 = currencies.get(self.curr2)[1]
        history.append(str(self.value) + ' ' + self.curr1 + ' '+ '='  + ' ' + str(round(self.value * rate1 * rate2, 2)) +  ' ' + self.curr2)
        return round(self.value * rate1 * rate2, 2)


    def deletehistory(self):
        return history.clear()




print(history)


