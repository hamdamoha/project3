function buildCharts() {
    // Retrieve the attack data from the Flask app

    var queryURL = "http://127.0.0.1:5500/visualisation/chart.js"

    d3.json(queryURL).then(function(data) {
      // Convert the data to an array of objects with "label" and "value" properties
      const chartData = data.map(function(d) {
        return {
          label: d.Attack,
          value: d.Count
        };
      });
  
      // Create a pie chart using Chart.js
      const ctx = document.getElementById("pie-chart").getContext("2d");
      new Chart(ctx, {
        type: "pie",
        data: {
          labels: chartData.map(d => d.label),
          datasets: [{
            data: chartData.map(d => d.value),
            backgroundColor: [
              "rgba(255, 99, 132, 0.8)",
              "rgba(54, 162, 235, 0.8)",
              "rgba(255, 206, 86, 0.8)",
              "rgba(75, 192, 192, 0.8)",
              "rgba(153, 102, 255, 0.8)",
              "rgba(255, 159, 64, 0.8)",
              "rgba(255, 99, 132, 0.8)",
              "rgba(54, 162, 235, 0.8)",
              "rgba(255, 206, 86, 0.8)",
              "rgba(75, 192, 192, 0.8)",
              "rgba(153, 102, 255, 0.8)",
              "rgba(255, 159, 64, 0.8)",
            ]
          }]
        },
        options: {
          responsive: true,
          title: {
            display: true,
            text: "Pokemon Attack Types"
          }
        }
      });
    });
  }
  
  // Call the buildCharts function when the DOM is loaded
  document.addEventListener("DOMContentLoaded", buildCharts);
  