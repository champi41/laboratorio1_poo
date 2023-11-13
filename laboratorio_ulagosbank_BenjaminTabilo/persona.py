class persona: 

  def __init__(self, nombre, fechaNacimiento, rut):

    self.__nombre = nombre
    self.__fechaNacimiento = fechaNacimiento
    self.__rut = rut

  def get_nombre(self):
    return self.__nombre

  def get_fechaNacimiento(self):
    return self.__fechaNacimiento
    
  def get_rut(self):
    return self.__rut

  def toString(self):

    print('Nombre: ', self.__nombre)
    print('Fecha de nacimiento: ', self.__fechaNacimiento)
    print('Rut: ', self.__rut)

  def esMayorDeEdad(self):
    
    if (self.__fechaNacimiento.year > (datetime.datetime.now().year - 18)):
      return True
    else:
      return False
