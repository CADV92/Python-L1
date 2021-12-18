# **Python Sin Miedo**

## **Métodos de compresión de listas y diccionarios**

### _List comprehensions_
```python
[elemento for elemento in iterable if condición]
```

```python
valores = [ i for i in range(1, 100000) if i % 36 == 0]
print(valores)
```

```python
def main():
    # squares = []
    # for i in range(1, 101):
    #     if i % 3 != 0:
    #         squares.append(i**2)

    squares = [ i**2 for i in range(1, 101) if i % 3 != 0]
    print(squares)

if __name__ == '__main__':
    main()
```

### _Dictionary comprehensions_
```python
{key: value for value in iterable if condición}
```

```python
dictionary = {i: i**0.5 for i in range(1, 1001) }
print(dictionary)
```


```python
def main():
    # my_dict = {}
    # for i in range(1, 101):
    #     if i % 3 != 0:
    #         my_dict[i] = i**3

    my_dict = {i: i**3 for i in range(1,101) if i % 3 != 0}
    print(my_dict)

if __name__ == '__main__':
    main()
```

## **Funciones anónimas _(lambda)_**

Son una forma anónima y muy corta de declarar funciones.

[Documentación Oficial](https://docs.python.org/es/3/reference/expressions.html#lambda)

```python
lambda argumentos: expresión
```

```python
# Funcion que recoge un número entero y devuelve su cuadrado
>> lambda_func = lambda x: x**2 
>> lambda_func(3)
9
```

```python
>> lambda_func = lambda x: True if x**2 >= 10 else False
>> lambda_func(3)
False
>> lambda_func(4)
True
```
```python
# Filtrar números impares (Tradicional)
>> mi_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>> filtrado = []

>> for num in mi_lista:
       if num % 2 != 0:
           filtrado.append(num)

>> print(filtrado)
[1, 3, 5, 7, 9]
```
```python
# Filtrar números impares (Lambda)
>> mi_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

>> filtrado = filter(lambda x: x % 2 != 0, mi_lista)

>> print(list(filtrado))
[1, 3, 5, 7, 9]
```

## **Funciones de orden superior**
Las funciones de orden superior son aquellas que reciben como parámetro otra función y hace algo con esta.

- `filter`
  
  Devuelve `True` or `False` según el valor esté dentro de los criterios buscados o no. En caso de que no cumpla con la condición, no será devuelto y la lista se verá reducida por este filtro.

  ```python
  filter(<funcion filtro>, <iterable>)
  ```
  ```python
  my_list = [1, 4, 5, 6, 9, 13, 19, 21]
  odd = list(filter(lambda x: x%2 != 0,my_list))

  print(odd)
  ```
- `map`
  
  A diferencia de `filter` ejecuta la función sobre cada uno de los elementos del iterable.
  
  ```python
  map(<funcion>, <iterable>)
  ```
  ```python
  my_list = [1, 2, 3, 4, 5]
  squares = list(map(lambda x: x**2, my_list))
  print(squares)
  ```
- `reduce`
  
  Reduce el iterable por medio de una función recibida como argumento.

  ```python
  reduce(<funcion reducción>, <iterable>)
  ```
  ```python
  from functools import reduce
  my_list = [2, 2, 2, 2, 2]
  allMultiplied = reduce(lambda a, b: a * b, my_list)
  print(allMultiplied)
  ```
  > _Nota: En el primer parámetro de nuestra función anónima sirve de variable totalizadora._

```python
DATA = [
    {
        'name': 'Mario',
        'age': 72,
        'organization': 'Chambita 1',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisa',
        'age': 33,
        'organization': 'Chambita 2',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Ulises',
        'age': 19,
        'organization': 'Chambita 1',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Chambita 1',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Chambita 1',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Chambita 3',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Chambita 4',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def run():

    # Comprehensions solutions
    all_python_devs = [worker["name"] for worker in DATA if worker["language"] == "python"]
    all_Chambita 1_workers = [worker["name"] for worker in DATA if worker["organization"] == "Chambita 1"]
    adults =  [worker["name"] for worker in DATA if worker["age"] > 18]
    # old_people = list(map(lambda worker: worker | {"old": worker["age"] > 70}, DATA))
    old_people = list(map(lambda worker: {**worker, **{"old": worker["age"] > 70}}, DATA))

    for worker in all_python_devs:
        print(worker)


if __name__ == '__main__':
    run()
```

```python
all_python_devs = list(filter(lambda worker: worker["language"] == "python", DATA))
all_python_devs = list(map(lambda worker: worker["name"], all_python_devs))

all_Chambita1_workers = list(filter(lambda worker: worker["organization"] == "Chambita 1", DATA))
all_Chambita1_workers = list(map(lambda worker: worker["name"], all_Chambita1_workers))

adults = list(filter(lambda worker: worker["age"] > 18, DATA))
adults = list(map(lambda worker: worker["name"], adults))

old_people = [worker | {"old": worker["age"] > 70} for worker in DATA]

for worker in all_python_devs:
    print(worker)
```
## **Errores**
Tipos de errores.
1. SintaxError
2. Exception

[Documentación Oficial](https://docs.python.org/es/3/tutorial/errors.html)

Consejos.
1. Leer el error.
2. Leer el traceback de abajo hacia arriba.

## **Debugging**
## **Control de Errores**

El control de errores se realiza a través de un bloque de código `try-except`.

```python
try:
    <BLOQUE DE SENTENCIAS TRY>
    ...
except:
    <LANZAMIENTO DE EXCEPCIONES>
    ...
```


```python
try:
    <BLOQUE DE SENTENCIAS TRY>
    ...
except:
    <LANZAMIENTO DE EXCEPCIONES>
    ...
else:
    <EN CASO NO OCURRAN EXCEPCIONES>
    ...
finally:
    <BLOQUE DE EJECUCIÓN FINAL>
    ...
```

### _Lanzamiento de excepciones - **raise**_

`raise` nos permite forzar la ocurrencia de una excepción específica.

```python
>>> raise NameError('Hola Clase!')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: Hola Clase!
```

```python
def duplica(num):
    try:
        if not isinstance(num,int):
            raise ValueError('No puede ingresar letras')
        return num*2
    except ValueError as ve:
        print(ve)
        return False
```

```python
def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def run():
    while True:
        try:
            num = int(input('Ingresa un número: '))
            if num < 0:
                raise ValueError
            print(divisors(num))
            print("Terminó mi programa")
            break
        except ValueError:
            print("Debes ingresar un entero positivo")


if __name__ == '__main__':
    run()
```

## **Assert statements**

Al manejar los errores es posible determinar afirmaciones, expresiones que afirman o condicionan el programa.

En caso la afirmación no se cumplma, devolverá un error.

```python
assert <CONDICIÓN>, <MENSAJE DE ERROR>
```

![Flujo Assert Statement](https://www.softwaretestinghelp.com/wp-content/qa/uploads/2021/05/working-of-the-Assertion-in-Python.png)


```python
def duplica(num):
    try:
        assert isinstance(num,int), "SOLO SE PERMITEN NÚMEROS ENTEROS!"
        return num*2
    except ValueError as ve:
        print(ve)
        return False
```

```python
def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def run():
    num = input('Ingresa un número: ')
    assert num.isnumeric(), "Debes ingresar un número"
    print(divisors(int(num)))
    print("Terminó mi programa")


if __name__ == '__main__':
    run()
```


## **Manipulación de archivos**

Manipular archivos es de suma importancia al momento de gestionar nuestros proyectos, podemos tratarlos como **archivos de texto** o **como un binario**.

### _Modos de apertura_
- `r -> Lectrura`
- `w -> Escritura (sobrescribe)`
- `a -> Escritura (añade)`


### _Método de apertura_
`with` Es un manejador contextual, nos ayuda a controlar el flujo del archivo (sirve para que el archivo no se dañe cuando existe algún cierre inesperado)

```python
with open(<ruta>, <modo_apertura>) as <nombre>
    ...
```

```python
def read():
    numbers = []
    # encoding='utf-8'
    with open("./archivos/numbers.txt", "r") as f: 
        for line in f:
            numbers.append(int(line))
    print(numbers)


def write():
    names = ["Juanjo", "Manuel", "Andrea", "Nicole", "Alessandra"]
    with open("./archivos/names.txt", "w") as f:
        for name in names: 
            f.write(name)
            f.write("\n")


def run():
    write()


if __name__ == '__main__':
    run()
```