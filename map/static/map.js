const map = L.map('map').setView([43.584, 39.723], 13);
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

var popup = L.popup();
var marker = L.marker();


function onMapClick(e) {
console.log(e)
    const lat = document.querySelector("#lat");
    const lng = document.querySelector("#lng");
    lat.value = e.latlng.lat;
    lng.value = e.latlng.lng;
    marker
        .setLatLng(e.latlng)
        .bindPopup("You clicked the map at " + e.latlng.toString())
        .openPopup()
        .addTo(map);
}

map.on('click', onMapClick);

