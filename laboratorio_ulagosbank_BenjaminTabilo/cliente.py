from persona import persona

class cliente(persona):

  def __init__(self, nombre, fechaNacimiento, rut, password, productos):
    
    super().__init__(nombre, fechaNacimiento, rut)
    self.password = password
    self.productos = productos
    
