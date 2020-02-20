import logging
from api import PixabayAPI
import sys
import threading

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

imagenes = '/home/concurrente/python-manipulando-imagenes-Emanuelr9/imagenes'
query = sys.argv[1]
cantidad= sys.argv[2]


api = PixabayAPI('15310694-79541d54c04910f8a3106dbd1', imagenes)

logging.info(f'Buscando {cantidad} imagenes de {query}')
urls = api.buscar_imagenes(query, cantidad)

for u in urls:
    logging.info(f'Descargando {u}')
    #api.descargar_imagen(u)
    threading.Thread(target=(lambda: api.descargar_imagen(u))).start()