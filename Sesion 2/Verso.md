# **Python Sin Miedo**

## **Variables en Python**

En Python las variables no necesitan declarse o definirse de antemano, para crear una variable solo debemos asignar un valor y luego empezar a usarlo.

La asignación se realiza con un signo igual (=).

`>>> identificador = [expresión]`

### **Asignaciones**
- #### _**Asignaciones simples**_
  -> Un valor a una variable
  <details open>
  <summary>Ejemplo</summary>

  ```python
  nombre = 'Christian Dávila'
  edad = 28
  curso = "PYTHON-L1"
  latlon = [-12.04318, -77.02824]
  origen = {
	  		'pais': 'Perú',
			  'ciudad': 'Lima',
			  'latlon': latlon,
			 }
  ```
  </details><br/>

- #### _**Asignaciones mútiples**_
  -> Valores a varias variables
  <details open>
  <summary>Ejemplo</summary>

  ```python
  latitude, longitude = [-12.04318, -77.02824]
  str_color1, str_color2 = 'Red', 'Blue'
  color_R, color_G, color_B = (255,0,0)
  clr1, clr2, clr3 = 'Red'
  ```
  </details><br/>

### **Literales y expresiones**
- #### _**Literales**_
  -> Información estática
  <details open>
  <summary>Ejemplo</summary>

  ```python
  precio = 150
  descuento = 0.2
  aplicar_descuento = True
  precio_final = 150 * (1 - 0.2)
  ```
  </details><br/>

- #### _**Expresiones**_
  -> Información dinámica
  <details open>
  <summary>Ejemplo</summary>

  ```python
  precio_final = precio * (1 - descuento)
  msg = "Precio Final " + precio_final
  ```
  </details><br/>

### **Keywords**

Son palabras reservadas que no pueden ser utilizadas como identificadores válidos.

|||||
| ----- | --- | -- | ---- |
| False | def | if | raise | 
| None | del | import | return |
|True | elif | in | try|
|and | else | is | while|
|as | except | lambda | with|
|assert | finally | nonlocal | yield|
|break | for | not | |
|class | from | or | |
|continue | global | pass| |

Comprobando si es keyword

```python
>>> import keyword
>>> keyword.iskeyword('red')
False
>>> keyword.iskeyword('as')
True
```

[PEP8 online](http://pep8online.com/checkresult)<br/><br/>

## **Tipos de datos**

Definen un conjunto de valores que tienen una serie de características y propiedades determinadas.

- Numéricos
  - Enteros `--> (int)`
  - De punto flotante `--> (float)`
  - Complejos `--> (complex) {<real> <imag>}`
- Cadena de caracteres `--> (str)`
- Booleanos `--> (bool)`
- Listas `--> (list)`
- Tuplas `--> (tuple)`
- Conjuntos `--> (set)`
- Diccionarios `--> (dict)`

> Podemos explorar el tipo de dato mediante `type()` e `isinstance()`.

## **Operadores lógicos y de comparación**

- Lógicos
  - `and`
  - `or`
  - `not`
- Comparación
  - `==`
  - `!=`
  - `>`
  - `<`
  - `>=`
  - `<=`

## **Estructuras de control de flujo**

El flujo natural de ejecución es desde la primera hacia la línea final, no obstante podemos modificarlo a través de estructuras especiales; permitiendo al programa el tomar uno u otro camino.

### Estructuras de control condicionales

Las estructuras de control condicionales se definen con la palabra reservada `if`, seguida de la expresión lógica que se someterá a evaluación, ejecutandose su bloque de instrucciones solo si el resultado evaluado es verdadero (`True`).

**`--> if`**
```python
if <EXPRESION>:
  <BLOQUE DE SENTENCIAS>
  ...
  print('Fin del Bloque')
```

**`--> if-else`**
```python
if <EXPRESION>:
  <BLOQUE DE SENTENCIAS>
  ...
  print('Fin del Bloque True')
else:
  <BLOQUE DE SENTENCIAS>
  ...
  print('Fin del Bloque False')
```

**`--> if-elif-else`**
```python
if <EXPRESION>:
  <BLOQUE DE SENTENCIAS>
  ...
  print('Fin del Bloque True')
elif <EXPRESION 2>:
  <BLOQUE DE SENTENCIAS>
  ...
  print('Fin del Bloque True del elif')
else:
  <BLOQUE DE SENTENCIAS>
  ...
  print('Fin del Bloque False')
```

**`--> Condicionales anidados`**
```python
if <EXPRESION>:
  if <EXPRESION 2>:
    <BLOQUE DE SENTENCIAS>
    ...
    print('Fin del Bloque True')
  elif <EXPRESION 3>:
    <BLOQUE DE SENTENCIAS>
    ...
    print('Fin del Bloque True del elif')
  else:
    <BLOQUE DE SENTENCIAS>
    ...
    print('Fin del Bloque False')
  ...
else:
  <BLOQUE DE SENTENCIAS>
  ...
  print('Fin del Bloque False')
```

### Estructuras de control iterativas

Las estructuras de control iterativas nos permiten repetir una porción de código, estor pueden ser del tipo definido o indefinido.

- Indefinido `--> while`
  > El número de iteraciones depende de la evalucación de la expresión, mientras sea `True` el bloque seguirá ejecutándose.
  > ```python
  > while <EXPRESION>:
  >   <BLOQUE DE SENTENCIAS>
  >   ...
  > ```
- Definido `--> for`
  > El número de iteraciones está establecido.
  >```python
  > for <VARIABLE> in <OBJETO ITERABLE>:
  >  <BLOQUE DE SENTENCIAS>
  >   ...
  > ```

#### _Las declaraciones break y continue_
- `break`
  
  _Rompe el ciclo, continuando el flujo del programa_

  ```python
  numeroMayor = -99999999
  contador = 0
  
  while True:
      numero = int (input ("Ingresa un número o escribe -1 para finalizar el programa:"))
      if numero == -1:
          break
      contador = 1
      if numero > numeroMayor:
          numeroMayor = numero
  
  if contador != 0:
      print("El número más grande es", numeroMayor)
  else:
      print("No ha ingresado ningún número") 
  ```

- `continue`
  
  _Salta a la siguiente iteración._

  ```python
  numeroMayor = -99999999
  contador = 0

  numero = int (input("Ingresa un número o escribe -1 para finalizar el programa:"))

  while numero != -1:
      if numero == -1:
          continue
      contador = 1

      if numero > numeroMayor:
          numeroMayor = numero
      numero = int (input ("Ingresa un número o escribe -1 para finalizar el programa:"))

  if contador:
      print("El número más grande es", numeroMayor)
  else:
      print("No ha ingresado ningún número") 
  ```

## **Funciones**

Las funciones son bloques de código que podemos reutilizar desde nuestro propio **código** o invocarlas a partir del **sistema integrado de Python** u otros **módulos preinstalados**.

### Definiendo nuestras funciones

Definimos funciones empleando la palabra reservada `def`.

```python
def <NOMBRE DE MI FUNCIÓN>:
  <
   BLOQUE DE SENTENCIAS DE
   LA FUNCIÓN
  >
  ...
```
```python
def mensaje():
    print("Ingresa un valor: ")

print("Se comienza aquí.")
mensaje()
print("Se termina aquí.")
```

### Parámetros y argumentos

```python
def suma(a, b):
  return a + b

a = 2
b = 6
res_suma = suma(a, b)
print(f'El resultado de {a} {b}:\n\t{res_suma}')
```

- ... posicionales
- ... con palabra clave
- ... predefinidos

### Documentando una función _(docstring)_

La documentación se establece utilizando comillas triples luego de definir la función.

```python
def suma(a, b):
  """
  Retorna la suma de 'a' y 'b'.
  resultado = a + b

  Ejemplo:
    >> suma(2,4)
    6
  """
  return a + b
```

Mediante la función `help` podemos visualizar la documentación.

```python
help(suma)
```
Ejemplo
```python
def fib(n):
    if n < 1:
         return None
    if n < 3:
        return 1

    elem1 = elem2 = 1
    sum = 0
    for i in range(3, n + 1):
        sum = elem1 + elem2
        elem1, elem2 = elem2, sum
    return sum

for n in range(1, 10):
    print(n, "->", fib(n))
```


Recursividad en funciones
```python
def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    return fib(n - 1) + fib(n - 2)
```

```python
def factorial(n):
    return 1 if (n==1 or n==0) else n * factorial(n - 1)

print(factorial(4))
```

```python
def fun(a):
    if a > 30:
        return 3
    else:
        return a + fun(a + 3)

print(fun(25))
```

## **Colecciones**
### _Tuplas_
Son objetos ordenados e inmutables, son definidas mediante `()`.
```python
# mi_tupla = (elementos,...)
latlon = (-12, -76)
```

### _Listas_
Son objetos ordenados y definidas mediante `[]`.
```python
# mi_lista = [elementos,...]
latlon = (-12, -76)
```


### _Diccionarios_
Son objetos no ordenados, se definen mediante `{}` y sus elementos están compuestos en un par `key-value`.
```python
# mi_diccionario = {key: value,...}
coordenadas = {
                'latitude': -12,
                'longitude': -76
              }
```
> _Consideraciones_
>  - Cada clave debe de ser **única**. No es posible tener una clave duplicada.
Una clave puede ser **un tipo de dato de cualquier tipo**: puede ser un número (entero o flotante), o incluso una cadena.
> - Un diccionario es una **herramienta de un solo sentido**. Si fuese un diccionario español-francés, podríamos buscar en español para encontrar su contraparte en francés mas no viceversa.

```python
grupo = {}

while True:
    nombre = input("Ingresa el nombre del estudiante (o exit para detenerse): ")
    if nombre == 'exit':
        break
    
    calif = int(input("Ingresa la calificación del alumno (0-10): "))
    
    if nombre in grupo:
        grupo[nombre] += (calif,)
    else:
        grupo[nombre] = (calif,)
        
for nombre in sorted(grupo.keys()):
    sum = 0
    contador = 0
    for calif in grupo[nombre]:
        sum += calif
        contador += 1
    print(nombre, ":", sum / contador)
```


### _Conjuntos_
Son objetos no ordenados, de valores no repetidos y definidas mediante `{}`.
```python
# mi_conjunto = {elementos,...}
números = {1,2,3,4,5,6}
```

```python
>>> colores = {'azul', 'rojo', 'blanco', 'blanco'}
>>> colores
{'rojo', 'azul', 'blanco'}
```