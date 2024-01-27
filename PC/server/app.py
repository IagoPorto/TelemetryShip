from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from sensors_RX import zenoh_sub
import csv
import os
import plotly.express as px
from datetime import datetime



app = Flask(__name__, template_folder='templates')
CORS(app)  

csv_directory = './csv_data'
##FACER Q SE NON EXISTE SE CREE
dist = zenoh_sub("sensors/dist")
accel = zenoh_sub("sensors/accel")
gyro = zenoh_sub("sensors/gyro")
magnet = zenoh_sub("sensors/magnet")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sensors/dist')
def get_dist():
    data = dist.get_data()
    print("GET distance")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
    save_to_csv('dist.csv', [timestamp, data])  # Garda o dato en dist.csv
    return jsonify({"distance": data})  

@app.route('/sensors/accel')
def get_accel():
    data = accel.get_data()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
    save_to_csv('accel.csv', [timestamp, data])  # Garda o dato en accel.csv
    return jsonify({"acceleration": data})  

@app.route('/sensors/gyro')
def get_gyro():
    data = gyro.get_data()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
    save_to_csv('gyro.csv', [timestamp, data])  # Garda o dato en gyro.csv
    return jsonify({"gyro": data})  

@app.route('/sensors/magnet')
def get_magnet():
    data = magnet.get_data()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
    save_to_csv('magnet.csv', [timestamp, data])  # Garda o dato en magnet.csv
    return jsonify({"magnet": data})  


def save_to_csv(filename, data):
    csv_path = os.path.join(csv_directory, filename)
    header_exists = os.path.isfile(csv_path)

    with open(csv_path, 'a', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        if not header_exists and filename == 'distancia':
            csv_writer.writerow(['Timestamp'] + ['ValueX'] + ['ValueY'] + ['ValueZ'])
        elif not header_exists and filename != 'distancia':
            csv_writer.writerow(['Timestamp'] + ['Value'])
        csv_writer.writerow(data)


@app.route('/visualizar_datos', methods=['POST'])
def visualizar_datos():

    # Obtener valores del formulario
    inicio_rango = datetime.strptime(request.form['inicio_rango'] + ":00.000000", "%Y-%m-%dT%H:%M:%S.%f")
    fin_rango = datetime.strptime(request.form['fin_rango'] + ":00.000000", "%Y-%m-%dT%H:%M:%S.%f")
    
    # Obtener la lista de archivos CSV seleccionados
    archivos_seleccionados = request.form.getlist('archivos')

    # Crear un diccionario para mapear los nombres de los archivos a las rutas
    archivos = {
        'distancia': './csv_data/dist.csv',
        'aceleracion': './csv_data/accel.csv',
        'giroscopio': './csv_data/gyro.csv',
        'magnetismo': './csv_data/magnet.csv'
    }

    # Lista para almacenar objetos fig
    figuras = []

    # Leer datos desde CSV solo para los archivos seleccionados
    for archivo in archivos_seleccionados:
        if archivo in archivos:
            with open(archivos[archivo], 'r') as csv_file:
                csv_reader = csv.reader(csv_file)
                header = next(csv_reader)
                timestamp_index = header.index('Timestamp')
                value_indices = [header.index(column) for column in header if column.startswith('Value')]

                data = []
                for row in csv_reader:
                    if archivo == 'distancia':
                        timestamp = row[timestamp_index]
                        value = row[value_indices[0]]
                        #value = [row[i] for i in value_indices]
                        data.append({'Timestamp': timestamp, 'Value': value})
                    else:
                        timestamp = row[timestamp_index]
                        values = [row[i] for i in value_indices]
                        data.append({'Timestamp': timestamp, 'ValueX': values[0], 'ValueY': values[1], 'ValueZ': values[2]})

            if archivo == 'distancia':
                #print([d for d in data])
                """ for dic in data:
                    for k in dic:
                        print(f'Clave: {k}, Valor: {dic[k]}') """
                datos_filtrados = [d for d in data if inicio_rango <= datetime.strptime(d['Timestamp'], "%Y-%m-%d %H:%M:%S.%f") <= fin_rango]
                figura = px.line(datos_filtrados, x='Timestamp', y='Value', title=f'{archivo} para el rango {inicio_rango} - {fin_rango}')
                figura.update_layout(yaxis_type="linear")
            else:
                print('HOLAA', [d for d in data])
                datos_filtrados = [d for d in data if inicio_rango <= datetime.strptime(d['Timestamp'], "%Y-%m-%d %H:%M:%S.%f") <= fin_rango]
                figura = px.line(datos_filtrados, x='Timestamp', y=['ValueX','ValueY','ValueZ'], title=f'{archivo} para el rango {inicio_rango} - {fin_rango}')
                figura.update_layout(yaxis_type="linear")
                plot_html = f"temp_plot_dist.html"
                figura.write_html(f"./{plot_html}")

            figuras.append(figura)

    # Convertir todas las figuras a HTML
    html_plots = [fig.to_html(full_html=False) for fig in figuras]
    
    return render_template('visualizacion.html', html_plots=html_plots)

    
if __name__ == '__main__':
    app.run(debug=True, port=5000)
