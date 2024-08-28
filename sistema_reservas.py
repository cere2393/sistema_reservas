usuarios_registrados = []
reservas = []

def registrar_usuario():
    """Permite registrar un nuevo usuario en el sistema."""
    print("\nRegistro de Usuario")
    nombre_usuario = input("Ingrese el nombre de usuario: ").strip()
    
    if nombre_usuario in usuarios_registrados:
        print("El nombre de usuario ya está registrado.")
    else:
        usuarios_registrados.append(nombre_usuario)
        print(f"Usuario '{nombre_usuario}' registrado con éxito.")

def reservar_viaje():
    """Permite a un usuario registrado reservar un viaje."""
    print("\nReservar un Viaje")
    nombre_usuario = input("Ingrese su nombre de usuario: ").strip()
    
    if nombre_usuario not in usuarios_registrados:
        print("El usuario no está registrado. Por favor, regístrese primero.")
        respuesta = input("¿Desea registrarse ahora? (s/n): ").strip().lower()
        if respuesta == 's':
            registrar_usuario()
        else:
            print("Debe registrarse para hacer una reserva.")
            return
    
    destino = input("Ingrese el destino del viaje: ").strip()
    fecha = input("Ingrese la fecha del viaje (en formato YYYY-MM-DD): ").strip()
    
    reservas.append({
        'usuario': nombre_usuario,
        'destino': destino,
        'fecha': fecha
    })
    print("Reserva realizada con éxito.")

def ver_reservas():
    """Permite a un usuario ver todas sus reservas."""
    print("\nVer Reservas")
    nombre_usuario = input("Ingrese su nombre de usuario: ").strip()
    
    if nombre_usuario not in usuarios_registrados:
        print("El usuario no está registrado.")
        return
    
    reservas_usuario = [reserva for reserva in reservas if reserva['usuario'] == nombre_usuario]
    
    if not reservas_usuario:
        print("No tiene reservas.")
    else:
        print("Sus reservas:")
        for i, reserva in enumerate(reservas_usuario, 1):
            print(f"{i}. Destino: {reserva['destino']}, Fecha: {reserva['fecha']}")

def cancelar_reserva():
    """Permite a un usuario cancelar una de sus reservas."""
    print("\nCancelar una Reserva")
    nombre_usuario = input("Ingrese su nombre de usuario: ").strip()
    
    if nombre_usuario not in usuarios_registrados:
        print("El usuario no está registrado.")
        return
    
    reservas_usuario = [reserva for reserva in reservas if reserva['usuario'] == nombre_usuario]
    
    if not reservas_usuario:
        print("No tiene reservas para cancelar.")
        return
    
    print("Sus reservas:")
    for i, reserva in enumerate(reservas_usuario, 1):
        print(f"{i}. Destino: {reserva['destino']}, Fecha: {reserva['fecha']}")
    
    try:
        index = int(input("Seleccione el número de la reserva que desea cancelar: ")) - 1
        if 0 <= index < len(reservas_usuario):
            reserva_a_cancelar = reservas_usuario[index]
            reservas.remove(reserva_a_cancelar)
            print("Reserva cancelada con éxito.")
        else:
            print("Número de reserva inválido.")
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número.")

def menu_principal():
    """Función principal que muestra el menú y maneja la interacción con el usuario."""
    while True:
        print("\n--- Menú Principal ---")
        print("1. Registrar un usuario")
        print("2. Reservar un viaje")
        print("3. Ver reservas")
        print("4. Cancelar una reserva")
        print("5. Salir")
        
        opcion = input("Seleccione una opción (1-5): ").strip()
        
        if opcion == '1':
            registrar_usuario()
        elif opcion == '2':
            reservar_viaje()
        elif opcion == '3':
            ver_reservas()
        elif opcion == '4':
            cancelar_reserva()
        elif opcion == '5':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción entre 1 y 5.")

if __name__ == "__main__":
    menu_principal()