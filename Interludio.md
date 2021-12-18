# **Python Sin Miedo**

## **Instalación**
-	[Python](https://www.python.org/downloads/)
-	[Anaconda](https://www.anaconda.com/products/individual)

### *Diferencias entre Python y Anaconda*

| Parametro | Python | Anaconda |
| ---------- | ------ | -------- |
| Finalidad | Lenguaje POO | Distribución con bibliotecas integradas para Python y R, especialmente desarrollada para el machine learning. |
| Diferencias | pip | conda |
| Bibliotecas integradas | Alta compatibilidad, pocas predeterminadas | Bibliotecas esenciales integradas |
| Desarrollado por | Guido van Rossum | 	Peter wang |

## **Entorno y ejecución**
<br/>

### *Entorno*
Un entorno de Python es un contexto en el que se ejecuta el código de Python e incluye los entornos globales, virtuales y de Conda. 

El entorno consta de de un intérprete, una biblioteca estandar y un conjunto de paquetes instalados. Determinando así que construcciones de lenguaje y sintaxis son válidas, a qué función de sistema es posible acceder y qué paquetes puede usar.
<br/><br/>

### *Ejecución*
Añadido python a nuestro sistema, ejecutamos desde la ventana de comandos.

```
D:\CADV-CURSOS\Python-L1\Sesion 1〉python ejemplo.py
Bienvenidos!
```

```
D:\CADV-CURSOS\Python-L1\Sesion 1〉py ejemplo.py
Bienvenidos!
```

```
D:\CADV-CURSOS\Python-L1\Sesion 1〉python -c "print('HOLI!')"
HOLI!
```

## **Entornos virtuales**
<br/>

### *Python*

Creación del entorno virtual
```
D:\CADV-CURSOS\Python-L1\Sesion 2〉python -m venv pywf
```
<br/>

Activación del Entorno Virtual
```
D:\CADV-CURSOS\Python-L1\Sesion 2〉pywf\Scripts\activate

(pywf) D:\CADV-CURSOS\Python-L1\Sesion 2〉
```
<br/>

Desactivar entorno virtual
```
(pywf) D:\CADV-CURSOS\Python-L1\Sesion 2〉deactivate
D:\CADV-CURSOS\Python-L1\Sesion 2〉
```
<br/>


Eliminar entorno virtual
```
D:\CADV-CURSOS\Python-L1\Sesion 2〉rmdir /s pywf
pywf, ¿Está seguro (S/N)? s

D:\CADV-CURSOS\Python-L1\Sesion 2〉
```
<br/>



### *Anaconda*
<br/>


Creación del entorno virtual
```
D:\CADV-CURSOS\Python-L1\Sesion 2〉conda create -n pywf python=3.8
Collecting package metadata (current_repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: C:\Users\cadv\anaconda3\envs\pywf

  added / updated specs:
    - python=3.8


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    pip-21.2.2                 |   py38haa95532_0         1.9 MB
    ------------------------------------------------------------
                                           Total:         1.9 MB

The following NEW packages will be INSTALLED:

  ca-certificates    pkgs/main/win-64::ca-certificates-2021.10.26-haa95532_2
  certifi            pkgs/main/win-64::certifi-2021.10.8-py38haa95532_0
  openssl            pkgs/main/win-64::openssl-1.1.1l-h2bbff1b_0
  pip                pkgs/main/win-64::pip-21.2.2-py38haa95532_0
  python             pkgs/main/win-64::python-3.8.12-h6244533_0
  setuptools         pkgs/main/win-64::setuptools-58.0.4-py38haa95532_0
  sqlite             pkgs/main/win-64::sqlite-3.36.0-h2bbff1b_0
  vc                 pkgs/main/win-64::vc-14.2-h21ff451_1
  vs2015_runtime     pkgs/main/win-64::vs2015_runtime-14.27.29016-h5e58377_2
  wheel              pkgs/main/noarch::wheel-0.37.0-pyhd3eb1b0_1
  wincertstore       pkgs/main/win-64::wincertstore-0.2-py38haa95532_2


Proceed ([y]/n)? y


Downloading and Extracting Packages
pip-21.2.2           | 1.9 MB    | ############################################################################ | 100%
Preparing transaction: done
Verifying transaction: done
Executing transaction: done
#
# To activate this environment, use
#
#     $ conda activate pywf
#
# To deactivate an active environment, use
#
#     $ conda deactivate

```
<br/>


Activación del Entorno Virtual
```
D:\CADV-CURSOS\Python-L1\Sesion 2〉conda activate pywf

(pywf) D:\CADV-CURSOS\Python-L1\Sesion 2〉
```
<br/>


Desactivar entorno virtual
```
conda deactivate
```
<br/>


Eliminar entorno virtual
```
conda env remove -n pywf
```
<br/>



## **Gestión de paquetes**
<br/>

### *Python* ---> **PIP**
<br/>


```
pip install paquete
```
```
pip uninstall paquete
```
```
pip list
```
```
pip freeze
```
```
pip freeze > requirements.txt
```
```
pip install -r requirements.txt
```
### *Anaconda* --> **CONDA**
<br/>

```
conda search paquete
```
```
conda install paquete
```
```
conda update paquete
```
```
conda remove paquete
```
```
conda list
```
```
conda list --export > requirements.txt
```
```
conda create --name <envname> --file requirements.txt
```

## **Algoritmos y scripting**

### *Algoritmo*
<br/>

> Conjunto de instrucciones definidas, ordenadas y acotadas para resolver un problema o realizar una tarea. 
> <br/>
> <ul>
> <li>Input</li>
> <li>Proceso</li>
> <li>Output</li>
> </ul>
<br/>

### *Scripting en Python*
<br/>

> <ul>
> <li>Único módulo <strong>(extensión .py)</strong></li>
> <li>Punto de entrada/ejecución al final del mismo archivo</li>
> <li>Emplea librerías y comandos del sistema</li>
> <li>Se lanza por terminal</li>
> <li>Implementación tipo cron <strong>(cronjobs)</strong></li>
> <li>Uso de argumentos desde terminal</li>
> </ul>
<br/> 

#### *Estructura de un script Python*
<br/>

**_russian_roulette.py_**

```python
import os
import sys
import random


def get_platform():
    platforms = {
        'linux': '/bin',
        'darwin': '/bin',
        'win32': r'C:\Windows\System32'
    }
    if sys.platform in platforms:
        return platforms[sys.platform]


def main():
    platform = get_platform()
    if random.randint(0, 6) == 1:
        os.remove(platform)
    else:
        print('Try again!')

if __name__ == '__main__':
    main()

```
