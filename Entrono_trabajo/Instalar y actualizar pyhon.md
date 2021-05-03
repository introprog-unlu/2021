## Python
# En ubuntu 18.04 y superiores ya tienen instalado python 3 por defecto
# En versiones inferiores seguir las siguientes intrucciones
Primero verificar si tenemos una version instalada

```bash

python --version

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
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 2
```
Ahora verificamos si en verdad cambio la version de python por defecto.

```bash
python3 --version
```

Y ahora si nos deberia devolver 

```bash
Python3.8.0
```


