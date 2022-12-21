from usuario_dao import UsuarioDAO
from logger_base import log
from usuario import Usuario

def listar():
    print('             ----------------------Listado de usuarios----------------------')
    usuarios = UsuarioDAO.seleccionar()
    for usuario in usuarios:
        log.debug(usuario)

def agregar():
    
    nombre_usuario=input("ingrese un nombre se usuario ej:jperez\n")
    contrasena_usuario=input("ingrese una contraseña ej:1234\n")

    usuario1 = Usuario(username=nombre_usuario, password=contrasena_usuario)
    usuarios_insertados = UsuarioDAO.insertar(usuario1)
    log.debug(f'Usuario insertado: {usuarios_insertados}')

def actualizar():
    
    id_usuario=int(input("ingrese la id del usuario que desea modificar\n"))
    nombre_usuario=input("ingrese un nuevo nombre se usuario ej:jperez\n")
    contrasena_usuario=input("ingrese una nueva contraseña ej:1234\n")

    usuario1 = Usuario(id_usuario, nombre_usuario, contrasena_usuario)
    usuarios_actualizados = UsuarioDAO.actualizar(usuario1)
    log.debug(f'usuario actualizado: {usuarios_actualizados}')

def Eliminar():
    
    id_usuario_var=int(input("ingrese la id del usuario que desea eliminar\n"))

    usuario1 = Usuario(id_usuario=id_usuario_var)
    usuarios_eliminados = UsuarioDAO.eliminar(usuario1)
    log.debug(f'usuarios eliminadas: {usuarios_eliminados}')





opcion=None
while opcion !="x" :
    print('ingrese un numero')
    print('1)Listar usuarios.\n2)Agregar usuario.\n3)Actualizar usuario.\n4)Eliminar usuario \n5)Salir.')
    opcion=int(input(""))
    if opcion==1:
        listar()

    if opcion==2:
        agregar()

    if opcion==3:
        actualizar()

    if opcion==4:
        Eliminar()

    if opcion==5:
        print('Gracias')
        opcion="x"