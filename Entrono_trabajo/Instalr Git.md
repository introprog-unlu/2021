## Instalar Git y conectarlo con gitHub

## Instalacion de Git

La instalacion de git es sencilla, y simplemente debemos ejecutar como sudo

```bash

sudo apt-get install git-all

```

Lo verificamos ejecutando 

```bash

git --version

```

y si obtenemos algo como git version 2.20.1 tendremos correctamente instalado git

# Configurar email y usuario

```bash

git config --global user.name "agrup"
git config --global user.email agustinrodriguez206@gmail.com

git config --list 

```

si todo sale bien tendremos una salida similar a la siguiente 

```bash

user.email=agustinrodriguez206@gmail.com.ar
user.name=agrup

```

orpimimos q para salir

