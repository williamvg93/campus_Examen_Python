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