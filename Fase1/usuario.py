class Usuario():
    def __init__(self,rol,nombre,apellido,telefono,correo,contrasena):
        self.rol = rol
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.correo = correo
        self.contrasena = contrasena
        self.factura = None #podria ser una lista de facturas
        self.peliculasFavoritas = None
        self.boleto = None