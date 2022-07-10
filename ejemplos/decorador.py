# decorador en python
def decorador(funcion):
  print("Antes de la función")
  funcion()
  print("Después de la función")
  return 'ok'


# @decorador
def funcion_original():
    print("Esta es la función original")

# print(funcion_original)
# decorador(funcion_original)

# otro ejemplo
# funciones decoradoras
def agregar_dos(funcion):
  def agregar_dos_aux(a, b):
    resultado = funcion(a,b)
    resultado += 2
    print(f'El resultado es: {resultado}')
    return 1
  return agregar_dos_aux


def agregar_tres(funcion):
  def agregar_tres_aux(*args, **kwargs):
    resultado = funcion(*args, **kwargs)
    resultado += 3
    print(f'El resultado es: {resultado}')
    return 1
  return agregar_tres_aux

def agregar_cuatro(funcion):
  def agregar_cuatro_aux(*args, **kwargs):
    resultado = funcion(*args, **kwargs)
    resultado += 4
    print(f'El resultado es: {resultado}')
    return 1
  return agregar_cuatro_aux

#funcion original

@agregar_cuatro
def suma(a,b):
  return a + b

print(suma(1,2))
# decorador = agregar_tres(suma)
# print(decorador(1,2))
# suma(1,2)
# agregar_dos_aux = agregar_dos(suma)
# agregar_tres_aux = agregar_tres(suma)
# agregar_cuatro_aux = agregar_cuatro(suma)
# print(suma_dos_aux(1,2))
# print(suma_tres_aux(1,2))
# print(suma_cuatro_aux(1,2))

