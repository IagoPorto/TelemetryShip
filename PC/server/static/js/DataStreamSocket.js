const socket = new WebSocket ("ws://localhost:8765");

socket.onmessage = (event) => {

    const distDiv = document.getElementById ("dist");
    const accelDiv = document.getElementById ("accel");
    const gyroDiv = document.getElementById ("gyro");
    const magnetDiv = document.getElementById ("magnet");

    const msg = event.data.split (";");

    distDiv.innerHTML = `<p> ${msg [0]} </p>`;
    accelDiv.innerHTML = `<p> ${msg [1]} </p>`;
    gyroDiv.innerHTML = `<p> ${msg [2]} </p>`;
    magnetDiv.innerHTML = `<p> ${msg [3]} </p>`;
};