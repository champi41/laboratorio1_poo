from cuenta import cuenta

class cuentaJoven(cuenta):
    
    def __init__(self, titular, saldo, movimientos, bonificacion):
        
      super().__init__(titular, saldo, movimientos)
      self.__bonificacion = bonificacion

    def get_bonificacion(self):
      
      return self.__bonificacion

    def set_bonificacion(self, newBonificacion):
      
      self.__bonificacion = newBonificacion

    def esTitularValido(self):
      pass  

    def bonificar(self):
      pass

    def toString(self):
      print('Titular: ', self.get_titular)
      print('saldo: ', self.get_saldo)
      print('movimientos: ', self.get_movimientos)
      print('bonificacion: ', self.get_bonificacion)
      
