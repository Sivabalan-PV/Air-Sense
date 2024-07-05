// Fetch data from the API
async function fetchData() {
    const response = await fetch('https://api.airquality.example.com/data?key=YOUR_API_KEY');
    const data = await response.json();
    return data;
}

// Create the chart
function createChart(data) {
    const ctx = document.getElementById('chart').getContext('2d');
    new Chart(ctx, {
        type: 'line',
        data: {
            labels: data.map(item => item.date),
            datasets: [{
                label: 'Air Quality',
                data: data.map(item => item.quality),
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 1
            }]
        }
    });
}

// Create the calendar
function createCalendar(data) {
    const calendarEl = document.getElementById('calendar');
    new FullCalendar.Calendar(calendarEl, {
        initialView: 'dayGridMonth',
        events: data.map(item => ({
            title: `Quality: ${item.quality}`,
            start: item.date,
            color: item.quality > 100 ? 'red' : 'green'  // Change color based on air quality
        }))
    }).render();
}

// Fetch data and create the chart and calendar
fetchData().then(data => {
    createChart(data);
    createCalendar(data);
});
