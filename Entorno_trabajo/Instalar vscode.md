## Instalar Visual Studio Code

# Descargar VSCode

Dirigirnos al sitio https://code.visualstudio.com/

Y descargamos el archivo .deb o .rpm segun nuesta version de sistema operativo
en este caso lo haremos para ubuntu, por eso descargaremos la opcion .deb
y recordamos el directorio donde lo guardamos, en este caso en ~/vscode con el nombre vscode.deb

Si lo queremos hacer directamente de la consola , primero creamos un directorio donde descargar VSCode
nos dirigimos a la carpeta y descargamos el .deb para instalar el editor

```bash

mkdir ~/vscode

cd ~/vscode/

wget  -c https://code.visualstudio.com/sha/download\?build\=stable\&os\=linux-deb-x64 -o vscode.deb

```

# Instalar Visual Studio Code

Estando el direcotrio donde se decargo el .deb  ejecutamos 
recuerda que el nombre del archivo puede no ser igual si salio alguna version nueva

```bash

sudo dpkg -i vscode.deb

```
nos va a pedir la contraseña de sudo, la colocamos y damos enter

Luego verificamos que todo salio bien, crearemos un directorio de trrabajo y abriremos vscode en esa carpeta

```bash

mkdir ~/IntroProg 

cd ~/IntroProg

code .
 
``` 

Esto deberia abrir el edito VS Code, en el directorio IntroProg




