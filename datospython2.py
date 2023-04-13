import json
from datetime import datetime

#ruta del archivo donde vamos a sacar un token
ruta_archivo = "/home/devasc/labs/devnet-src/parsing/myfile.json"

#abrir el archivo JSON en la maquina virtual
with open(ruta_archivo,'r') as archivo:
    #leer el contenido del archivo JSON
    ourjson = json.load(archivo)

#obtener el valor del token y la fecha de caducidad del JSON
token = ourjson['access_token']
fecha_caducidad = datetime.fromisoformat(str(ourjson['expires_in']))

#obtener la fecha y hora actual
fecha_actual = datetime.now()

#calcular la cantidad del tiempo que queda antes que el token caduque
tiempo_restante = fecha_caducidad - fecha_actual



#print(json_file)
#print(json_file['access_token'])

