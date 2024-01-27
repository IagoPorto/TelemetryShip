const ctx = document.getElementById('myChart').getContext('2d');
const alertSound = document.getElementById('alertSound');


const myChart = new Chart(ctx, {
  type: 'line',
  data: {
    labels: [], 
    datasets: [{
      label: 'Distance',
      borderColor: '#ffcefb',
      pointBorderColor: '#ffcefb',
      data: [],
      fill: false,
    }]
  },
  options: {
    scales: {
      x: [{
        type: 'linear', 
        position: 'bottom',
        color: '#00e4ff',
      }],
      y: [{
        type: 'linear',
        position: 'left',
      }]
    }
  }
});

function alertSoundFunction(value) {
  if (value < 20) {
    if (alertSound.paused) {
      alertSound.play();
    }
  } else {
    alertSound.pause();
    alertSound.currentTime = 0; 
  }
}

var index = -1
function updateGraph(data) {
    alertSoundFunction(data)
    index++;
    myChart.data.labels.push(index); 
    myChart.data.datasets[0].data.push(data);
    const maxDataPoints = 100;
    if (myChart.data.labels.length > maxDataPoints) {
      myChart.data.labels.shift();
      myChart.data.datasets[0].data.shift();
    }
    myChart.update();
}