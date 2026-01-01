document.addEventListener("DOMContentLoaded", () => {
  // Shared Chart configurations
  const chartOptions = {
    responsive: true,
    plugins: {
      legend: {
        labels: { color: "#ffffff" },
      },
    },
    scales: {
      y: {
        beginAtZero: true,
        grid: { color: "rgba(255, 255, 255, 0.1)" },
        ticks: { color: "#b3b3b3" },
      },
      x: {
        grid: { display: false },
        ticks: { color: "#b3b3b3" },
      },
    },
  };

  // 1. City Chart
  const cityCtx = document.getElementById("cityChart").getContext("2d");
  new Chart(cityCtx, {
    type: "bar",
    data: {
      labels: ["Delhi", "Mumbai", "Kolkata", "Bangalore"],
      datasets: [
        {
          label: "Positive Cases",
          data: [130, 125, 120, 132], // Sample data, would ideally be fetched
          backgroundColor: "rgba(0, 242, 255, 0.6)",
          borderColor: "#00f2ff",
          borderWidth: 1,
        },
        {
          label: "Total People",
          data: [250, 248, 252, 252],
          backgroundColor: "rgba(255, 255, 255, 0.1)",
          borderColor: "rgba(255, 255, 255, 0.3)",
          borderWidth: 1,
        },
      ],
    },
    options: chartOptions,
  });

  // 2. Gender Chart
  const genderCtx = document.getElementById("genderChart").getContext("2d");
  new Chart(genderCtx, {
    type: "doughnut",
    data: {
      labels: ["Male", "Female"],
      datasets: [
        {
          data: [248, 259],
          backgroundColor: ["#00f2ff", "#7000ff"],
          borderWidth: 0,
        },
      ],
    },
    options: {
      ...chartOptions,
      scales: {}, // Doughnut doesn't use x/y scales
    },
  });

  // 3. Age Distribution Chart (Sample bins)
  const ageCtx = document.getElementById("ageChart").getContext("2d");
  new Chart(ageCtx, {
    type: "line",
    data: {
      labels: [
        "0-10",
        "11-20",
        "21-30",
        "31-40",
        "41-50",
        "51-60",
        "61-70",
        "71+",
      ],
      datasets: [
        {
          label: "Cases by Age",
          data: [45, 62, 85, 90, 75, 60, 50, 40],
          borderColor: "#00f2ff",
          backgroundColor: "rgba(0, 242, 255, 0.1)",
          fill: true,
          tension: 0.4,
        },
      ],
    },
    options: chartOptions,
  });

  // 4. Cough Severity Chart
  const coughCtx = document.getElementById("coughChart").getContext("2d");
  new Chart(coughCtx, {
    type: "bar",
    data: {
      labels: ["Mild", "Strong"],
      datasets: [
        {
          label: "Covid Positive",
          data: [245, 262],
          backgroundColor: ["#00f2ff", "#ff0055"],
        },
      ],
    },
    options: chartOptions,
  });
});
