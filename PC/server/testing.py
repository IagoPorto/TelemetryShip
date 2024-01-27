'''
Este script crea no directorio csv_data 4 ficheiros csv con datos random 
para as probas de visualizar datos.

Primeiro executar este script e logo o visualizar_datos.py

app_with_csv.py está pendente de probar
'''

import os
import csv
from datetime import datetime
import random
import time

csv_directory = './csv_data'  # Reemplaza 'tu_directorio_de_csv' con el directorio deseado

if not os.path.exists(csv_directory):
    # Crea el directorio si no existe
    os.makedirs(csv_directory)

def save_to_csv(filename, data):
    csv_path = os.path.join(csv_directory, filename)

    header_exists = os.path.isfile(csv_path)
    with open(csv_path, 'a', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        if not header_exists and filename == 'dist.csv':
            csv_writer.writerow(['Timestamp'] + ['Value'])
        elif not header_exists:
            csv_writer.writerow(['Timestamp'] + ['ValueX'] + ['ValueY'] + ['ValueZ'])
        csv_writer.writerow(data)

# Crear 50 filas de datos aleatorios para cada archivo
for _ in range(50):
    dist_data = [datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"), random.randint(1, 100)]  # Cambia el rango según tu necesidad
    accel_data = [datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)]
    gyro_data = [datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"), random.randint(1, 100), random.randint(-100, 100), random.randint(1, 100)]
    magnet_data = [datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)]
    #timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S") 

    time.sleep(1)

    save_to_csv('dist.csv', dist_data)
    save_to_csv('accel.csv', accel_data)
    save_to_csv('gyro.csv', gyro_data)
    save_to_csv('magnet.csv', magnet_data)
