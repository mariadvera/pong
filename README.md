# pong
Recreacion del juegp clásico PONG con pygame.


## como crear un entorno virtual
supongamos que quiero crear un entorno virtual con el nombre -env-.

'''
#en windows 
python -m venv env

#en mac/linux
python3 -m venv env
'''

## como activar el entorno virtual
'''
#en windows 
.\env\Scripts\activate

#en mac/linux
source ./env/bin/activate

'''


## gestor de paquetes
Instalar un paquete nuevo: `pip install <nombre del paquete>` 

activar el entornoantes de instalar

- listar los paquetes instalados: ` pip list `
-listar paquetes en formato de dependencias: `pip freeze`

- si quiero redireccionar  la salida >nombre del archivo donde estara ala salida
-requirment.txt es el stardand que se encuentra en python con las dependencias

-para guardarlo en el archivo de dependencias : `pip freeze> rewquirements.txt`

## como desactivar el entorno virtual
''deactivate
'''
## como eliminar el entorno virtual

Basta con eliminar el directorio