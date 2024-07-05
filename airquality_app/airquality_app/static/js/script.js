const apiKey = 'b39212e529f3396b2c21ed4d75f0f7459edb7894a06692e4f05d8cfd7fd23d3d';
const apiUrl = 'https://api.ambeedata.com';

// Replace with the desired location coordinates
const latitude =  lat;
const longitude = lon;

async function getAirQualityData(latitude, longitude) {
    
    try {
        const response = await fetch(`${apiUrl}/latest/by-lat-lng?lat=${latitude}&lng=${longitude}`, {
            headers: {
                'Content-Type': 'application/json',
                'x-api-key': apiKey,
            },
        });

        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error fetching air quality data:', error);
    }
}
function displayAirQuality(data) {
    const station = data.stations[0];
    const locationElement = document.getElementById('locationData');
    const aqiElement = document.getElementById('aqiData');
    locationElement.textContent = `${station.city}, ${station.state}, ${station.country}`;
    aqiElement.textContent = station.AQI;
    

    // Add more elements and data as needed
}
getAirQualityData(latitude, longitude)

    .then(data => {
        console.log('Air quality data:', data);
        // Display data on the dashboard
    });

displayAirQuality(data)
    .then(data => {
        console.log('Air quality data:', data);
        displayAirQuality(data);
    });
    /*
// Update every 5 minutes (adjust as needed)
setInterval(() => {
    getAirQualityData(latitude, longitude)
        .then(data => {
            console.log('Air quality data:', data);
            displayAirQuality(data);
        });
}, 300000);
*/