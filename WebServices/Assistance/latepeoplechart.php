<?php
require_once('latepeople.php');
?>
<link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.8.0/Chart.min.css" media="screen" />
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.8.0/Chart.min.js"></script>
<canvas id="myChart" width="500" height="500"></canvas>
<script>
// var ctx = document.getElementById('myChart').getContext('2d');
var ctx = document.getElementById('myChart');
var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        // labels: ['Llegadas a tiempo', 'Llegadas tarde', 'Salidas antes de tiempo', 'Salidas puntuales'],
        datasets: [{
            label: 'Llegadas a Tiempo (%)',
            data: [
              <?php
              $x=0;
              foreach($listRespuesta as $dat){
                if($x == 0) {
                  print("'".(($dat[0]/$countin)*100)."'");
                  $x=1;
                }else {
                  print(",'".(($dat[0]/$countin)*100)."'");
                }
              }
              ?>
            ],
            backgroundColor: 'rgba(0, 143, 57, 0.2)',
            borderColor: 'rgba(0, 143, 57, 1)',
            borderWidth: 1
        },
        {
            label: 'LLegadas Tarde (%)',
            data: [
              <?php
              $x=0;
              foreach($listRespuesta2 as $dat){
                if($x == 0) {
                  print("'".(($dat[0]/$countin)*100)."'");
                  $x=1;
                }else {
                  print(",'".(($dat[0]/$countin)*100)."'");
                }
              }
              ?>
            ],
            backgroundColor: 'rgba(248, 0, 0, 0.2)',
            borderColor: 'rgba(248, 0, 0, 1)',
            borderWidth: 1
        },
        {
            label: 'Salidas Antes de Tiempo (%)',
            data: [
              <?php
              $x=0;
              foreach($listRespuesta3 as $dat){
                if($x == 0) {
                  print("'".(($dat[0]/$countout)*100)."'");
                  $x=1;
                }else {
                  print(",'".(($dat[0]/$countout)*100)."'");
                }
              }
              ?>
            ],
            backgroundColor: 'rgba(248, 0, 0, 0.2)',
            borderColor: 'rgba(248, 0, 0, 1)',
            borderWidth: 1
        },
        {
            label: 'Salidas puntuales (%)',
            data: [
              <?php
              $x=0;
              foreach($listRespuesta4 as $dat){
                if($x == 0) {
                  print("'".(($dat[0]/$countout)*100)."'");
                  $x=1;
                }else {
                  print(",'".(($dat[0]/$countout)*100)."'");
                }
              }
              ?>
            ],
            backgroundColor: 'rgba(0, 143, 57, 0.2)',
            borderColor: 'rgba(0, 143, 57, 1)',
            borderWidth: 1
        },
        ]
    },
    options: {
      legend: { display: true },
      title: {
        display: true,
        text: 'Llegadas y Salidas en (%)'
      },
      responsive: true,
      scales: {
          yAxes: [{
              ticks: {
                  beginAtZero: true
              }
          }]
      }
    }
});
</script>