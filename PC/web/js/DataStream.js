const distUrl = 'http://localhost:5000/sensors/dist';
const accelUrl = 'http://localhost:5000/sensors/accel';
const gyroUrl = 'http://localhost:5000/sensors/gyro';
const magnetUrl = 'http://localhost:5000/sensors/magnet';

function updateData(elementId, data, title) {
  const element = document.getElementById(elementId);
  element.textContent = `${title}: ${data}`;
}

function fetchDataAndUpdate() {
    fetch(distUrl)
        .then(response => response.json())
        .then(data => {
            updateData('dist', data.distance, 'Distance');
            updateGraph(data.distance);
        })
        .catch(error => console.error(error));

    fetch(accelUrl)
        .then(response => response.json())
        .then(data => updateData('accel', data.acceleration, 'Accelerometer'))
        .catch(error => console.error(error));

    fetch(gyroUrl)
        .then(response => response.json())
        .then(data => updateData('gyro', data.gyro,'Gyroscope'))
        .catch(error => console.error(error));

    fetch(magnetUrl)
        .then(response => response.json())
        .then(data => updateData('magnet', data.magnet, 'Magnetometer'))
        .catch(error => console.error(error));
}

setInterval(fetchDataAndUpdate, 1000);

fetchDataAndUpdate();
