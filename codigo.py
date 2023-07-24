from operator import getitem
from collections import OrderedDict

""" try:
    patDatDay = input('Enter the Day, Exampe "5": ')
    veriDataType(patDatDay, 'num', )
    while not((patDatDay >= 1) and (patDatDay <= 31)):
        patDatDay = int(input('Enter the Day, remember the day must be a number between "1" and "31" : '))
    patDatMonth = int(input('Enter the Month, Exampe "10": '))
    while not((patDatMonth >= 1) and (patDatMonth <= 12)):
        patDatMonth = int(input('Enter the Month, remember the Month must be a number between "1" and "12" : '))
    patDatYear = int(input('Enter the Year, Exampe "2023": '))
    while not((patDatYear >= 1900) and (patDatYear <= 2030)):
        patDatYear = int(input('Enter the year, remember the year must be a number between "1900" and "2030" : '))
    patDate = f'{patDatDay}/{patDatMonth}/{patDatYear}'
    print(f'patDate = {patDate}')
except ValueError as e:
    print(e) 
    
    
    patTimHour = input('Enter the Hour, example "12": ')
    while not((patTimHour >= 6) and (patTimHour <= 20)):
        patDatYear = int(input('Enter the Hour, remember the Hour must be a number between "6" and "20" : '))
    patTimMinu = input('Enter the Minutes, example "30": ')
    while not((patTimMinu >= 0) and (patTimMinu <= 59)):
        patDatYear = int(input('Enter the Minutes, remember the Minutes must be a number between "6" and "20" : '))
    patTime = f'{patTimHour}:{patTimMinu}'
    print(f'patTime = {patTime}')"""
    
''' newData = dict(OrderedDict(sorted(data.items(), key = lambda x: getitem(x[1], 'Name'))))
print('')
print('-'*90)
print('-'*37 + ' Citas Médicas ' + '-'*38)
print('-'*90)
print('{:^17}{:^20}{:^25}{:^25}'.format('Id', 'Name of Patient', 'Date of Appoinment', 'Time of Appointment' ))
for keyAp, valAp in newData.items():
    #print(f'{keyAp} -- {valAp}')
    print('{:^17}{:^20}{:^25}{:^25}'.format(keyAp, valAp['Name'], valAp['Date'], valAp['Time']))
print('')
waitExit() '''
    
    
dici = {
            "1": {
                "Name": "william",
                "Date": "2023-08-05",
                "Time": 52500.0,
                "Reason": "prueba"
            },
            "2": {
                "Name": "carlos",
                "Date": "2023-11-30",
                "Time": 26100.0,
                "Reason": "prueba 2"
            },
            "3": {
                "Name": "eduardo",
                "Date": "2022-10-30",
                "Time": 26100.0,
                "Reason": "prueba 3"
            }
    }
#print(sorted(dici, key=lambda x: x['Date']))
#print(sorted(dici, key=operator.itemgetter('Date')))
newDicci = dict(OrderedDict(sorted(dici.items(), key = lambda x: getitem(x[1], 'Date'), reverse=True)))
newDicci1 = OrderedDict(sorted(dici.items(), key = lambda x: getitem(x[1], 'Date')))
print(newDicci)
print(newDicci1)