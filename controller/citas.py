import model.citas as citModel
import datetime
import operator


def waitExit():
    contExit = True
    while contExit:
        rtaExit = input('Enter "Y" to exit: ').lower()
        contExit = False if rtaExit == 'y' else True

def veriDataType(data, typeDat):
    try:
        if typeDat == 'num':
            nuevoDato = int(typeDat)
        if type(data) == type:
            return True
    except ValueError as e:
        print(e)
        return False

def AddCita(fileName):
    citModel.checkFile(fileName)
    data = citModel.getData(fileName)
    contAdd = 0
    if len(data) < 1:
        contAdd = 1
    else:
        contAdd = len(data) + 1 
    patId = contAdd
    print(contAdd)

    patName = input('Name of Patient: ')
    print('Appointment Date')
    contDate = True
    while contDate:
        try:
            patDate = datetime.date(day=int(input('enter day: ')), month=int(input('enter month: ')), year= int(input('enter year: '))).isoformat()
            #print(f'{patDate} -> {type(patDate)}')
            #print(type(patDate))
            #print(patDate)
            #print(datetime.datetime.fromisoformat(patDate))
            #print(type(datetime.datetime.fromisoformat(patDate)))
            contDate = False
        except ValueError as e:
            print(e)
        except Exception as e:
            print(e)
    
    print('Appointment Time')
    contHour = True
    while contHour:
        try:
            patTime = datetime.timedelta(hours=int(input('Enter the appointment Hour: ')), minutes=int(input('Enter the appointment Minutes: ')))
            #print(f'{patTime} -> {type(patTime)}')
            patTime = datetime.timedelta.total_seconds(patTime)
            #print(patTime)
            #print(type(patTime))
            contHour = False
        except ValueError as e:
            print(e)
        except Exception as e:
            print(e)
    
    patReason = input('Reason for the Appointment: ')
    data[patId] = {
        'Name' : patName,
        'Date' : patDate,
        'Time' : patTime,
        'Reason' : patReason,
    }
    print(data)
    citModel.addData(fileName, data)
    
    

def updateCita(fileName):
    citModel.checkFile(fileName)
    data = citModel.getData(fileName)
    if len(data) < 1:
        print('Data needs to be added to edit !!')
    else:
        idEdit = input('Enter the appointment id: ')
        if idEdit in data:
            for keyDat, valDat in data[idEdit].items():
                try:
                    rtakey = input(f'Do you want to edit the {keyDat}, enter "Y" for Yes or "N" for not!!! :').lower()
                    if rtakey == 'y':
                        if keyDat == 'Date':
                            contDate = True
                            while contDate:
                                try:
                                    valDat = datetime.date(day=int(input('enter day: ')), month=int(input('enter month: ')), year= int(input('enter year: '))).isoformat()
                                    contDate = False
                                except ValueError as e:
                                    print(e)
                                except Exception as e:
                                    print(e)
                        elif keyDat == 'Time':
                            contHour = True
                            while contHour:
                                try:
                                    valDat = datetime.timedelta(hours=int(input('Enter the appointment Hour: ')), minutes=int(input('Enter the appointment Minutes: ')))
                                    valDat = datetime.timedelta.total_seconds(valDat)
                                    contHour = False
                                except ValueError as e:
                                    print(e)
                                except Exception as e:
                                    print(e)
                        else:
                            valDat = input(f'Enter the new {keyDat}: ')
                            while len(valDat) < 1:
                                valDat = input(f'Enter the new {keyDat}, the data must have more than one Character!!! : ')
                        data[idEdit][keyDat] = valDat
                except Exception as e:
                    print(e)             
            citModel.addData(fileName, data)  
        else:
            print(f'The id = {idEdit} does not exist in the db¡¡')
    waitExit()       
        
def listData(fileName):
    citModel.checkFile(fileName)
    data = citModel.getData(fileName)
    print(data)
    print(len(data))
    if len(data) < 1:
        print('There are no medical appointments in the DB !!')
    else:
        print('')
        print('-'*90)
        print('-'*37 + ' Citas Médicas ' + '-'*38)
        print('-'*90)
        print('{:^17}{:^20}{:^25}{:^25}'.format('Id', 'Name of Patient', 'Date of Appoinment', 'Time of Appointment' ))
        for keyAp, valAp in data.items():
            #print(f'{keyAp} -- {valAp}')
            print('{:^17}{:^20}{:^25}{:^25}'.format(keyAp, valAp['Name'], valAp['Date'], valAp['Time']))
        print('')
    waitExit()
    
def deleteApp(fileName):
    citModel.checkFile(fileName)
    data = citModel.getData(fileName)
    if len(data) < 1:
        print('There are no medical appointments in the DB !!')
    else:
        try:    
            idEdit = input('Enter the appointment id: ')
            if idEdit in data:
                print(data[idEdit])
                data.pop(idEdit)
                print(data)
            else:
                print(f'The id = {idEdit} does not exist in the db¡¡')
        except Exception as e:
            print(e)
    citModel.deleteData(fileName, data)
    waitExit()
        