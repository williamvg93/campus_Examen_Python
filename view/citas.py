import controller.citas as citCont

def citasView():
    contCitasMenu = True
    while contCitasMenu:
        print('-'*15 + ' Citas Médicas ' + '-'*15)
        print('1) Add Cita \n2) Edit Cita \n3) Delete Cita \n4) List Citas \n5) Exit App')
        try:
            rtaCitaMen = int(input('Enter the number of the option you want: '))
            if rtaCitaMen == 1:
                citCont.AddCita('CentroMedico')
            elif rtaCitaMen == 2:
                citCont.updateCita('CentroMedico')
            elif rtaCitaMen == 3:
                citCont.deleteApp('CentroMedico')
            elif rtaCitaMen == 4:
                citCont.listData('CentroMedico')
            elif rtaCitaMen == 5:
                contCitasMenu = False
            else:
                print('Enter a valid option !!!')
        except ValueError as e:
            print('Error !!!, Only numbers are allowed !!!')
        except Exception as e:
            print(e)