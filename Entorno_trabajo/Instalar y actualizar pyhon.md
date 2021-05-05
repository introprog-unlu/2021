## Python
# En ubuntu 18.04 y superiores ya tienen instalado python 3 por defecto
# En versiones inferiores seguir las siguientes intrucciones
Primero verificar si tenemos una version instalada

```bash

python3 --version

```

Esto nos retornara la version de python instalada , si tenemos python
con una version 3 o superior podemos trabajar con esa version o actualizarla.
Si no tenemos python instalado o una version inferior deberemos actualizarla.

# Instalar Python

En este ejemplo vamos a instalar Pythin 3.8 

```bash

sudo add-apt-repository ppa:deadsnakes/ppa 

```

```bash
sudo apt update 
```

```bash
sudo apt install python3.8
```

Verificar si termino exitosamente

```bash

python3 --version

```

esto deberia retornarnos 

```bash
Python 3.8.0
```

o los numeros de version instalada.

# Actualizar Python
Actualizar la version es identico a instalarlo pero con algunos pasos extras
primero si verificamos la version 

```bash
python3 --version
```

veremos que nos sigue devolviendo la version anterior, por eso lo que debemos hacer es indicar que queremos
a la version 3.8 por defecto con el siguiente comando

```bash
sudo update-alternatives --config python3 
```
Estos nos retornara un cuadro donde seleccionaremos la version de python que queremos

```
Existen 2 opciones para la alternativa python3 (que provee /usr/bin/python3).

  Selección   Ruta                Prioridad  Estado
------------------------------------------------------------
  0            /usr/bin/python3.7   2         modo automático
* 1            /usr/bin/python3.7   2         modo manual
  2            /usr/bin/python3.8   2         modo manual

Pulse <Intro> para mantener el valor por omisión [*] o pulse un número de selección:
```
seleccionamos la version que queremos, en mi caso seleccion 2 y oprimo enter

Ahora verificamos si en verdad cambio la version de python por defecto.

```bash
python3 --version
```

Y ahora si nos deberia devolver 

```bash
Python3.8.0
```

en caso de querer cambiar nuevamente la version repetimos el paso anterior y elegimos la version que queremos


