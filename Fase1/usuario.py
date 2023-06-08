class Usuario:
    def __init__(self, nombre, apellido , telefono, correo, password, rol = "cliente"):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.correo = correo
        self.password = password
        self.rol = rol