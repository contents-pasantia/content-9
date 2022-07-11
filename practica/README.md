1. Escribir una función llamada contrasenaValida que reciba un string y retorne true si el string es igual a "2Fj(jjbFsuj" o "eoZiugBf&g9". De lo contrario debe retornar false.
    ejemplo
    ```python
        # código de prueba
        print(contrasenaValida("2Fj(jjbFsuj")) # true
        print(contrasenaValida("eoZiugBf&g9")) # true
        print(contrasenaValida("hola")) # false
        print(contrasenaValuda("")) # false
    ```
2. Escribir una función llamada calcularImpuestos que reciba dos argumentos numéricos: edad e ingresos. Si edad es igual o mayor a 18 y los ingresos son iguales o mayores a 1000 debe retornar ingresos * 40%. De lo contrario retornar 0.

    ejemplo
    ```python
        # código de prueba
        print(calcularImpuestos(18, 1000)) # 400
        print(calcularImpuestos(40, 10000)) # 4000
        print(calcularImpuestos(17, 5000)) # 0
        print(calcularImpuestos(30, 500)) # 0
    ```
3. Escribe una función llamada likes que reciba un número y retorne un string utilizando el formato de K para miles y M para millones.

    Por ejemplo:

    1400 se convierte en 1K
    34,567 se convierte en 34K
    7’456,345 se convierte en 7M.
    Si el número es menor a 1000 se debe devolver el mismo número como un string.

    ejemplo
    ```python
    # código de prueba
    print(likes(983)) # "983"
    print(likes(1900)) # "1K"
    print(likes(54000)) # "54K"
    print(likes(120800)) # "120K"
    print(likes(25222444)) # "25M"
    ```
4. El índice de masa corporal (IMC), o BMI por sus siglas en inglés, es un valor que       determina la cantidad de grasa de una persona.

    El BMI se calcula con la siguiente formula: peso / altura^2

    Escribir una función llamada bmi que reciba dos argumentos: peso y altura, y retorne un string con las siguientes posibilidades:

    "Bajo de peso" si el BMI < 18.5
    "Normal" si está entre 18.5 y 24.9
    "Sobrepeso" si está entre 25 y 29.9
    "Obeso" si es igual o mayor a 30
    
    ejemplo:
    ```python
        # código de prueba
        print(bmi(65, 1.8)) # "Normal"
        print(bmi(72, 1.6)) # "Sobrepeso"
        print(bmi(52, 1.75)) #  "Bajo de peso"
        print(bmi(135, 1.7)) # "Obeso"
    ```