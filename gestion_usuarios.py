import os
import json
import getpass  # Para ocultar la entrada de la contraseña
import hashlib  # Para hashear la contraseña
from test_registro import *

nombre_archivo = "registros.json"

def menuIngreso():
    print("¡Bienvenido al organizador de estudio!")
    ingreso = input("¿Posee cuenta? (S/N): ").lower()
    ingreso_validado = validacion_sn(ingreso)

    if ingreso_validado in ["si", "s"]: 
        while True:  # Permitir que el usuario vuelva a intentar ingresar credenciales
            print("Por favor ingrese sus datos")
            user = input("Usuario: ")
            password = getpass.getpass("Contraseña: ")  # Ocultar la entrada de la contraseña
            if validacion_credenciales(user, password):
                break  # Salir del bucle si las credenciales son correctas
            else:
                print("Credenciales incorrectas. Intente de nuevo.")
    else:
        creacion = input("¿Desea crear una cuenta? (S/N): ").lower()
        ingreso_validado = validacion_sn(creacion)
        if ingreso_validado in ["si", "s"]: 
            crear_datos()
        else:
            print("¡Hasta luego!")
            exit()

def validacion_sn(dato_validar):
    if dato_validar not in ["si", "s", "no", "n"]:
        dato_validar = input("Ingrese una opción correcta (S/N): ").lower()
        return validacion_sn(dato_validar)
    else:
        return dato_validar

def cargar_datos():
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, 'r') as archivo:
            return json.load(archivo)
    return {"usuarios": []}  # Si no existe el archivo, devolvemos una estructura vacía

def crear_datos():
    print("Por favor ingrese sus datos para crear una cuenta")
    
    while True:
        user = input("Usuario: ").strip()  # Usar .strip() para eliminar espacios en blanco
        
        # Pedir contraseña dos veces
        password = getpass.getpass("Contraseña: ")  # Ocultar la entrada de la contraseña
        password_confirm = getpass.getpass("Confirme la Contraseña: ")  # Confirmar contraseña

        # Validar entradas
        if not validar_entradas(user, password, password_confirm):
            print("Por favor, intente de nuevo.")
            continue  # Volver a pedir las entradas

        # Verificar si el usuario ya existe
        if verificar_usuario_existente(user):
            print("Por favor, intente de nuevo.")
            continue  # Volver a pedir las entradas

        # Crear nueva entrada
        datos_nuevos = {
            "user": user,
            "password": hash_password(password)  # Hashear la contraseña
        }

        # Intentar agregar el nuevo usuario al archivo JSON
        if agregar_usuario_a_archivo(datos_nuevos):
            print(f"Cuenta creada exitosamente para el usuario: {user}")
            break  # Salir del bucle al crear la cuenta exitosamente
    cuestionario()
def validar_entradas(user, password, password_confirm):
    """Valida que el nombre de usuario y la contraseña no estén vacíos y que la contraseña tenga al menos 6 caracteres."""
    if not user or not password or not password_confirm:
        print("Error: El nombre de usuario y la contraseña no pueden estar vacíos.")
        return False
    if len(password) < 8:
        print("Error: La contraseña debe tener al menos 8 caracteres.")
        return False
    if password != password_confirm:
        print("Error: Las contraseñas no coinciden.")
        return False
    return True

def hash_password(password):
    """Devuelve el hash de la contraseña usando SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

def verificar_usuario_existente(user):
    """Verifica si el usuario ya existe."""
    mensaje = validacion_credenciales(user, "", check_only=True)  # No se necesita la contraseña
    if mensaje == "existe":
        print(f"Error: El usuario '{user}' ya existe. Intenta con otro nombre.")
        return True
    return False

def agregar_usuario_a_archivo(datos_nuevos):
    """Agrega un nuevo usuario al archivo JSON."""
    # Cargar datos existentes
    datos_existentes = cargar_datos()
    
    # Agregar el nuevo usuario a la lista
    datos_existentes["usuarios"].append(datos_nuevos)

    # Intentar guardar los datos actualizados en el archivo JSON
    try:
        with open(nombre_archivo, 'w') as archivo:
            json.dump(datos_existentes, archivo, indent=4)
        return True
    except IOError as e:
        print(f"Error al guardar los datos en el archivo: {e}")
        return False

def validacion_credenciales(user, password, check_only=False):
    registros = cargar_datos()
    for registro in registros.get("usuarios", []):
        if check_only:
            if registro.get("user") == user:
                return "existe"  # Usuario ya existe
        else:
            # Verificar la contraseña hasheada
            if registro.get("user") == user and registro.get("password") == hash_password(password):
                print("Acceso permitido: Usuario y contraseña correctos.")
                return True  # Credenciales correctas
    if not check_only:
        print("Acceso denegado: Usuario o contraseña incorrectos.")
    return False  # Credenciales incorrectas

# Iniciar el menú cuando se ejecuta el programa
if __name__ == "__main__":
    menuIngreso()
