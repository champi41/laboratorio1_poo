from persona import persona

class ejecutivo(persona):

  def __ini__(self, nombre, fechaNacimiento, rut, usuario, password):
    
    super().__init__(nombre, fechaNacimiento, rut)
    self.usuario = usuario
    self.password = password
    
