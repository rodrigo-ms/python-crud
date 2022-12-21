from conexion import Conexion
from cursor_del_pool import CursorDelPool
from usuario import Usuario
from logger_base import log

class UsuarioDAO:
    '''
    DAO (Data Access Object)
    CRUD (Create-Read-Update-Delete)
    '''
    _SELECCIONAR = 'SELECT * FROM usuario ORDER BY id_usuario'
    _INSERTAR = 'INSERT INTO usuario(username, password) VALUES(%s, %s)'
    _ACTUALIZAR = 'UPDATE usuario SET username=%s, password=%s WHERE id_usuario=%s'
    _ELIMINAR = 'DELETE FROM usuario WHERE id_usuario=%s'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
           # log.debug('seleccionando usuarios')
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            usuarios = []
            for registro in registros:
                usuario = Usuario(registro[0], registro[1], registro[2])
                usuarios.append(usuario)
            return usuarios

    @classmethod
    def insertar(cls, usuario):
        with CursorDelPool() as cursor:
            valores = (usuario.username, usuario.password)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'Usuario insertado: {usuario}')
            return cursor.rowcount

    @classmethod
    def actualizar(cls, usuario):
        with CursorDelPool() as cursor:
            valores = (usuario.username, usuario.password, usuario.id_usuario)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'Usuario actualizado: {usuario}')
            return cursor.rowcount

    @classmethod
    def eliminar(cls, usuario):
        with CursorDelPool() as cursor:
            valores = (usuario.id_usuario,)
            cursor.execute(cls._ELIMINAR, valores)
            log.debug(f'usuario eliminado: {usuario}')
            return cursor.rowcount

if __name__ == '__main__':
    # Insertar un registro
#    usuario1 = Usuario(username='bmunozs', password='1234')
#    usuarios_insertados = UsuarioDAO.insertar(usuario1)
#    log.debug(f'Usuario insertado: {usuarios_insertados}')

    # Actualizar un registro
#    usuario1 = Usuario(1, 'vsepulveda', '9050')
#    usuarios_actualizados = UsuarioDAO.actualizar(usuario1)
#    log.debug(f'Personas actualizadas: {usuarios_actualizados}')

    # Eliminar un registro
#    usuario1 = Usuario(id_usuario=3)
#    usuarios_eliminados = UsuarioDAO.eliminar(usuario1)
#    log.debug(f'usuarios eliminadas: {usuarios_eliminados}')

    # Seleccionar objetos
    usuarios = UsuarioDAO.seleccionar()
    for usuario in usuarios:
        log.debug(usuario)