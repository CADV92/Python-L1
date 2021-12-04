# **Python Sin Miedo**

## **Variables en Python**

En Python las variables no necesitan declarse o definirse de antemano, para crear una variable solo debemos asignar un valor y luego empezar a usarlo.

La asignación se realiza con un sigono igual $(=)$.

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

