class Coordenadas:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def distancia(self, otra_coordenada):
    x_diff = (self.x - otra_coordenada.x) ** 2 
    y_diff = (self.y - otra_coordenada.y) ** 2  
    return (x_diff + y_diff)**0.5 # Raiz cuadrada

if __name__ == '__main__':
  coord_1 = Coordenadas(1, 2)
  coord_2 = Coordenadas(3, 4)

  print(coord_1.distancia(coord_2)) # ejecuta el método distancia
  print(isinstance(coord_2, Coordenadas)) # comprobar si es una instancia de Coordenadas