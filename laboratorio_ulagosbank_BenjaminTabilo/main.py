#Integrantes Samuel Delgado, Camilo Mansilla y Benjamin Tabilo

from persona import persona
from cliente import cliente
from ejecutivo import ejecutivo
from cuenta import cuenta
from cuentaJoven import cuentaJoven

if __name__ == '__main__':

  tipoP = input('Ingrese (1) si es cliente o (2) si es ejecutivo: ')
  if tipoP == '1':
    productoBancario = input('Ingrese el nombre del producto bancario ((1) para tarjeta debito, (2) para tarjeta corriente o (3) para tarjeta de credito): ')
    cliente1 = cliente(input('Ingrese nombre: '), input('Ingrese fecha de nacimiento: '), input('Ingrese rut: '), input('Ingrese contraseña: '), productoBancario)

    tipoMovimiento = input('presione (1) para depositar o (2) para retirar: ')

    if tipoMovimiento == 1:
      cliente1.depositar(input('Ingrese monto a depositar: '))
      print('Su saldo actual es: ', cliente1.get_saldo())
    elif tipoMovimiento == 2:
      cliente1.retirar(input('Ingrese monto a retirar: '))
      print('Su saldo actual es: ', cliente1.get_saldo())
    else:
      print('Opcion invalida')
    
  elif tipoP == '2':
    ejecutivo1 = ejecutivo(input('Ingrese nombre: '), input('Ingrese fecha de nacimiento: '), input('Ingrese rut: ' ), input('Ingrese usuario: '), input('ingrese su contraseña: '))

    opcionEjecutivo = input('Ingrese (1) para crear cliente y ejecutivo o (2) para crear cuenta y/o cuenta joven: ')
  else:
    print('Ingrese un tipo de persona valido')


    
  
