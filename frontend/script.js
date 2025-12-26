const company = "Hubspot"; // dynamically from user input
const source = "g2";       // "g2", "capterra", "trustradius"

fetch("http://127.0.0.1:5000/scrape", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({
    company: "Hubspot",  // or dynamically from user input
    source: "g2"         // "g2", "capterra", or "trustradius"
  })
})

.then(res => res.json())
.then(data => {
  const tableBody = document.querySelector("tbody");
  if (!tableBody) return console.error("Table body not found");
  tableBody.innerHTML = "";

  let ratings = { 5: 0, 4: 0, 3: 0, 2: 0, 1: 0 };

  data.forEach(item => {
    const rating = Math.round(item.rating) || 0;
    if (rating >= 1 && rating <= 5) ratings[rating]++;

    const row = `
      <tr>
        <td>${item.product || ""}</td>
        <td>${item.reviewer || ""}</td>
        <td>${item.rating || ""} ⭐</td>
        <td>${item.title || ""}</td>
        <td>${item.description || ""}</td>
      </tr>
    `;
    tableBody.innerHTML += row;
  });

  drawChart(ratings);
})
.catch(err => console.error(err));

function drawChart(ratings) {
  const ctx = document.getElementById("chart").getContext("2d");

  new Chart(ctx, {
    type: "doughnut",
    data: {
      labels: ["5⭐", "4⭐", "3⭐", "2⭐", "1⭐"],
      datasets: [{
        data: [
          ratings[5] || 0,
          ratings[4] || 0,
          ratings[3] || 0,
          ratings[2] || 0,
          ratings[1] || 0
        ],
        backgroundColor: [
          "#4ade80",
          "#60a5fa",
          "#facc15",
          "#fb923c",
          "#ef4444"
        ]
      }]
    }
  });
}

