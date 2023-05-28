# proyecto final modulo 4

import os # Libreria de sistema
import csv # para usar el archicho .cvs


vehiculos = []
message = 'respuesta invalida'

class Vehiculo:
    def __init__(self,_marca, _modelo, _num_ruedas, _tipo_vehiculo):
        self.marca = _marca
        self.modelo = _modelo
        self.num_ruedas = _num_ruedas
        self.tipo_vehiculo = _tipo_vehiculo
    
    def crear_vehiculo(vehiculo):
        vehiculos.append(vehiculo)
        
    def leer_vehiculos():
        return vehiculos
    
    def cls_vehiculos():
        vehiculos.clear()
    
    def escribir_csv(vehiculos):
        
        if len(vehiculos) == 0:
            print("***** No hay vehículos registrados *****") 
            return
        
        print("\n***** Vehículos registrados *****")
    
        cont = 0
        with open('vehiculos.csv', 'a', newline='') as myCsv:
            writer = csv.writer(myCsv, delimiter=',')
            for item in vehiculos:
                if isinstance(item, Automovil):
                    if isinstance(item, Particular):
                        writer.writerow([item.tipo_vehiculo, item.marca, item.modelo, item.num_ruedas,
                                        item.tipo_automovil, item.velocidad, item.cilindrada, item.num_puestos])
                    elif isinstance(item, Carga):
                        writer.writerow([item.tipo_vehiculo, item.marca, item.modelo, item.num_ruedas,
                                    item.tipo_automovil, item.velocidad, item.cilindrada, item.capacidad_carga])
                elif isinstance(item, Bicicleta):
                    if isinstance(item, Motocicleta):
                        writer.writerow([item.tipo_vehiculo, item.marca, item.modelo, item.num_ruedas,
                                    item.tipo_bici, item.uso, item.num_radios, item.cuadro, item.motor])
                    else:
                        writer.writerow([item.tipo_vehiculo, item.marca, item.modelo, item.num_ruedas,
                                    item.tipo_bici, item.uso])
                cont= cont + 1

        print(f"Se registraron {cont} vehiculos en total.")
        
    def leer_datos_csv():
        file = 'vehiculos.csv'
        path = os.path.join(file)  #metodo que busca la ruta del archivo#
        auto = []
        carga = []
        moto = []
        bici = []
        if os.path.exists(path):
            with open(path) as archivo_csv:
                reader = csv.reader(archivo_csv) # abre el contenido del archivo legible e iterable#
                for item in reader:
                    if item[0].startswith('auto'): 
                        auto.append({
                            'marca': item[1],
                            'modelo': item[2],
                            'num_ruedas': item[3],
                            'tipo_automovil': item[4],
                            'velocidad': item[5],
                            'cilindrada': item[6],
                            'puestos': item[7]
                            })
                    elif item[0].startswith('camion'):
                        carga.append({
                            'marca': item[1],
                            'modelo': item[2],
                            'num_ruedas': item[3],
                            'tipo_automovil': item[4],
                            'velocidad': item[5],
                            'cilindrada': item[6],
                            'capacidad': item[7]
                            })
                    elif item[0].startswith('moto'):
                        moto.append({
                            'marca': item[1],
                            'modelo': item[2],
                            'num_ruedas': item[3],
                            'tipo_bici': item[4],
                            'uso': item[5],
                            'num_radios': item[6],
                            'cuadro': item[7],
                            'motor': item[8]
                            })
                    else:
                        bici.append({
                            'marca': item[1],
                            'modelo': item[2],
                            'num_ruedas': item[3],
                            'tipo_bici': item[4],
                            'uso': item[5]
                            })
            print('\n================== LISTADO DE VEHICULOS REGISTRADOS===============')
            print('\nVEHICULOS PARTICULARES:\n***********************')            
            for item in auto:
                print(f"Marca: {item['marca']:<15} Modelo: {item['modelo']:<15} Nro.Ruedas: {item['num_ruedas']:<3} Velocidad Km/h: {item['velocidad']:<5} Cilindrada: {item['cilindrada']:<5} Nro. Puestos: {item['puestos']}")
                
            print('\nVEHICULOS DE CARGA:\n*******************')
            
            for item in carga:
                print(f"Marca: {item['marca']:<15} Modelo: {item['modelo']:<15} Nro.Ruedas: {item['num_ruedas']:<3} Velocidad Km/h: {item['velocidad']:<5} Cilindrada: {item['cilindrada']:<5} Capacidad de Carga: {item['capacidad']}")
            
            print('\nMOTOCICLETAS:\n*************')
            for item in moto:
                print(f"Marca: {item['marca']:<15} Modelo: {item['modelo']:<15} Nro.Ruedas: {item['num_ruedas']:<3} Tipo: {item['uso']:<7} Motor: {item['motor']:<5} Cuadro: {item['cuadro']:<5} Nro. Radios: {item['num_radios']}")
                
            print('\nBICICLETAS:\n***********')    
            for item in bici:
                print(f"Marca: {item['marca']:<15} Modelo: {item['modelo']:<15} Nro.Ruedas: {item['num_ruedas']:<3} Tipo: {item['uso']}")    
                
             
            
            archivo_csv.close()
            
            continuar = input('\n*** Presione Enter para continuar *** ')
            pass
        else:
            print(f'Error: No existe el archivo {file}')
    
class Automovil(Vehiculo):
    def __init__(self, _marca, _modelo, _num_ruedas, _tipo_vehiculo, _tipo_automovil, _velocidad, _cilindrada):
        super().__init__(_marca, _modelo, _num_ruedas, _tipo_vehiculo)
        self.tipo_automovil = _tipo_automovil
        self.velocidad = _velocidad
        self.cilindrada = _cilindrada

class Particular(Automovil):
    def __init__(self, _marca, _modelo, _num_ruedas, _tipo_vehiculo, _tipo_automovil, _velocidad, _cilindrada, _num_puestos):
        super().__init__(_marca, _modelo, _num_ruedas, _tipo_vehiculo, _tipo_automovil, _velocidad, _cilindrada)
        self.num_puestos = _num_puestos

class Carga(Automovil):
    def __init__(self, _marca, _modelo, _num_ruedas, _tipo_vehiculo, _tipo_automovil, _velocidad, _cilindrada, _capacidad_carga):
        super().__init__(_marca, _modelo, _num_ruedas, _tipo_vehiculo, _tipo_automovil, _velocidad, _cilindrada)
        self.capacidad_carga = _capacidad_carga

class Bicicleta(Vehiculo):
    def __init__(self, _marca, _modelo, _num_ruedas, _tipo_vehiculo, _tipo_bici, _uso):
        super().__init__(_marca, _modelo, _num_ruedas, _tipo_vehiculo)
        self.tipo_bici = _tipo_bici
        self.uso = _uso

class Motocicleta(Bicicleta):
    def __init__(self, _marca, _modelo, _num_ruedas, _tipo_vehiculo, _tipo_bici, _uso, _num_radios, _cuadro, _motor):
        super().__init__(_marca, _modelo, _num_ruedas, _tipo_vehiculo, _tipo_bici, _uso)
        self.num_radios = _num_radios
        self.cuadro = _cuadro
        self.motor = _motor

if __name__ == '__main__':
    while True:
        print("\n============ Menú ===============")
        print("[1] Registrar vehículo")
        print("[2] Listar Vehiculos por Tipo")
        print("[3] Verificar Instancias clase Motocicleta")
        print("[0] Salir del Menú")
        opcion = input("\nIngrese una opción: ")

        if opcion == '0':
            break

        if opcion == '1':
            print("\n==== Registrar Datos del Vehículo =====")
            while True:
                try:
                    cant2 = int(input('Presione [0] para ir al menú principal\nIngrese el numero de vehiculos a Registrar: '))
                    if cant2 > 0:
                        for cant in range(1, cant2 + 1):
                            print('\n****************************\nDatos del vehiculo numero:', cant, '\n')
                            marca = input('\nIngrese la marca del vehiculo: ')
                            modelo = input('\nIngrese el Modelo: ')
                            num_ruedas =''
                            while num_ruedas not in [2, 4, 6, 8, 10, 12]:
                                try:
                                    num_ruedas = int(input('\nIngrese el numero de ruedas [2], [4], [6], [8], [10] o [12]: '))
                                    
                                    if num_ruedas > 3 and num_ruedas < 13:
                                        tipo_vehiculo = ''
                                        while tipo_vehiculo not in ['a', 'c']:
                                            tipo_vehiculo = input('\nIngrese [a] para automovil o [c] para vehiculos de carga: ')
                                            
                                            while True:
                                                try:
                                                    velocidad = int(input('\nIngrese la velocidad en Km/h: '))
                                                    break
                                                except:
                                                    pass
                                                                    
                                            while True:
                                                try:
                                                    cilindrada = int(input('\nIngrese el cilindraje en cc: '))
                                                    break
                                                except:
                                                    pass
                                            
                                        if tipo_vehiculo == 'a':
                                            tipo_vehiculo = 'auto'
                                            tipo_automovil = 'particular'
                                            while True:
                                                try:
                                                    num_puestos = int(input("\nIngrese el número de puestos: "))
                                                    break
                                                except:
                                                    pass
                                        
                                            vehiculo = Particular(marca, modelo, num_ruedas, tipo_vehiculo, tipo_automovil, velocidad, cilindrada, num_puestos)
                                        if tipo_vehiculo == 'c':
                                            tipo_vehiculo = 'camion'
                                            tipo_automovil = 'carga'
                                            while True:
                                                try:
                                                    capacidad_carga = int(input('\nInserte capacidad de carga en Kg: '))
                                                    break
                                                except:
                                                    pass
                                            
                                            vehiculo = Carga(marca, modelo, num_ruedas, tipo_vehiculo, tipo_automovil, velocidad, cilindrada, capacidad_carga)
                                    elif num_ruedas == 2:
                                        
                                        tipo_bici = ''
                                        while tipo_bici not in ['b', 'm']:
                                            tipo_bici = input('\nSeleccione [b] bicicleta, [m] para motocicleta: ')

                                        uso = ''
                                        while uso not in ['u', 'c']:
                                            uso = input('\nSeleccione [u] urbana, [c] carrera: ')
                                        if uso == 'u':
                                            uso = 'urbana'
                                        else:
                                            uso = 'carrera'

                                        if tipo_bici == 'b':
                                            tipo_bici ='bicicleta'
                                            tipo_vehiculo = 'bici'
                                            vehiculo = Bicicleta(marca, modelo, num_ruedas, tipo_vehiculo, tipo_bici, uso)
                                        else:
                                            while True:
                                                try:
                                                    num_radios = int(input('\nInserte el número de Radio: '))
                                                    break
                                                except:
                                                    pass
                                                
                                            cuadro = input('\nInserte tipo de Cuadro: ')
                                            motor = input('\nTipo de Motor: ')
                                            tipo_vehiculo = 'moto'
                                            tipo_bici = 'motocicleta'
                                            vehiculo = Motocicleta(marca, modelo, num_ruedas, tipo_vehiculo, tipo_bici, uso, num_radios, cuadro, motor)
                                            
                                    Vehiculo.crear_vehiculo(vehiculo)
                                    
                                except:
                                    continue
                        Vehiculo.escribir_csv(Vehiculo.leer_vehiculos())
                        Vehiculo.cls_vehiculos()
                    else:
                        break
                except:
                    print()
           
        elif opcion == '2':
            Vehiculo.leer_datos_csv()

        elif opcion == '3':
            motocicleta = Motocicleta('Suzuki', 'GSX250', '2', 'moto', 'motocicleta', 'urbana', 25, '4t', '310v')

            print('\nVerificacion de instancia de la clase Motocicleta:')
            print('Motocicleta es intancia con relación a Vehículo:', isinstance(motocicleta, Vehiculo)) 
            print('Motocicleta es intancia con relación a Vehículo:', isinstance(motocicleta, Automovil)) 
            print('Motocicleta es intancia con relación a Vehículo:', isinstance(motocicleta, Particular)) 
            print('Motocicleta es intancia con relación a Vehículo:', isinstance(motocicleta, Carga)) 
            print('Motocicleta es intancia con relación a Vehículo:', isinstance(motocicleta, Bicicleta)) 
            print('Motocicleta es intancia con relación a Vehículo:', isinstance(motocicleta, Motocicleta),'\n') 
        else:
            print('Opción inválida. Intente nuevamente.')
            
    print('\nGracias por su visita... Good bye\n')

