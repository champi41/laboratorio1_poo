
class cuenta():

  def __init__(self, titular, saldo, movimientos):

    self.titular = titular
    self.__saldo = saldo
    self.movimientos = movimientos


  def deposito(self, monto):

    if monto > 0:
      self.saldo += monto
      self.movimientos.append(monto)

  def retiro(self, monto):

    if monto > 0:
      if monto <= self.saldo:
        self.saldo -= monto
        self.movimientos.append(-monto)
      else:
        print('No hay saldo suficiente')

  def registrarMovimiento(self, monto):
    pass 

  
    
    
