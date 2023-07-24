import json

def getData(fileName):
    try:
        with open(f'data/{fileName}.json', 'r') as f:
            data = json.load(f)
            return data
    except Exception as e:
        print(e)

def checkFile(fileName):
    try:
        with open(f'data/{fileName}.json', 'r'):    
            print('File exists !!')
            pass
    except FileExistsError as e:
        print('Error file Exists')
        print(e)
    except FileNotFoundError as e:
        print('Error FileNotFound')
        print(e)
        with open(f'data/{fileName}.json', 'w') as f:
            json.dump({}, f, indent=4)
            
def addData(fileName, newData):
    try:
        with open(f'data/{fileName}.json', 'r') as f:
            oldData = json.load(f)    
            print(f'datos Antiguos: {oldData}')
            oldData.update(newData)
            print(f'datos nuevos: {oldData}')
        with open(f'data/{fileName}.json', 'w') as f:
            json.dump(oldData, f, indent=4)
    except Exception as e:
        print(e)

def deleteData(fileName, data):
    try:
        with open(f'data/{fileName}.json', 'w') as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        print(e)
        

