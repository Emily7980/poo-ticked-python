#Emily Torres

from administrar_ticked import AdministrarTicked
def menu():
    print('==================')
    print('NOMBRE: Emily Torres')
    print('==================')
    print('Bienvenido al sistema de tickeds')
    print('==================')
    print('1. Agregar tickeds')
    print('2. Listar tickeds')
    print('3. Editar tickeds')
    print('4. Eliminar tickeds')
    print('5. Priorizar tickeds')
    print('6. Salir')
    print('==================')
def principal():
    administrador = AdministrarTicked
    while True:
        menu()
        opcion = input('Por favor ingrese una opción: ')
        if opcion == '1':
            nombre = input('Nombre del ticked: ')
            fecha = input('Ingrese la fecha (DD-MM-YY): ')
            prioridad = input('Indique la prioridad (1, 2, 3): ')
            administrador.agregar_ticked(nombre,fecha,prioridad)
        elif opcion == '2':
            tickeds = administrador.listar_tickeds()
            for i in tickeds:
                print(f'{i.id}-{i.nombre}-{i.fecha}-{i.prioridad}')
        elif opcion == '3':
            print('Falta implementar Editar Tickeds')
        elif opcion == '4':
            print('Falta implementar Eliminar Tickeds')
        elif opcion == '5':
            print('Falta implementar Priorizar Tickeds')
        elif opcion == '6':
            print('Gracias por unsar el sistema')
            break
        else:
            print('Opción invalida, vuelva a intentar')
principal()