class Automovil:
  '''
    clase automovil
    atributos: marca, modelo, color
  '''
  def __init__(self, marca, modelo, color):
    self.marca = marca
    self.modelo = modelo
    self.color = color
    self._estado = 'en_reposo'
    self._motor = Motor(cilindros=4)

  def acelerar(self, tipo='despacio'):
    if tipo == 'despacio':
      self._motor.inyectar_gasolina(10)
      self._estado = 'en_movimiento'
    elif tipo == 'rapido':
      self._motor.inyectar_gasolina(20)
      self._estado = 'en_movimiento'
    else:
      raise ValueError('Tipo de aceleracion no reconocido')


class Motor:
  '''
    clase motor
    atributos: cilindros, tipo
  '''
  def __init__(self, cilindros, tipo = 'gasolina'):
    self.cilindros = cilindros
    self.tipo = tipo

  def inyecta_gasolina(self,cantidad):
    pass