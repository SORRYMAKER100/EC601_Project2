let map, pano, directionsRenderer, directionsService, autocompleteStart, autocompleteEnd, placesService;

function initMapAndAutocomplete() {
    map = new google.maps.Map(document.getElementById('map'), {
        center: { lat: -34.397, lng: 150.644 },
        zoom: 8
    });

    pano = new google.maps.StreetViewPanorama(
        document.getElementById('pano'), {
            position: { lat: -34.397, lng: 150.644 },
            pov: { heading: 34, pitch: 10 }
        }
    );

    directionsRenderer = new google.maps.DirectionsRenderer();
    directionsService = new google.maps.DirectionsService();
    directionsRenderer.setMap(map);
    directionsRenderer.setPanel(document.getElementById('right-panel'));

    autocompleteStart = new google.maps.places.Autocomplete(document.getElementById('start'));
    autocompleteEnd = new google.maps.places.Autocomplete(document.getElementById('end'));
    placesService = new google.maps.places.PlacesService(map);

    autocompleteStart.bindTo('bounds', map);
    autocompleteEnd.bindTo('bounds', map);
}

function planRoute() {
    let startAddr = document.getElementById('start').value;
    let endAddr = document.getElementById('end').value;
    let selectedMode = document.getElementById('mode').value;
    let radiusInKm = document.getElementById('radius').value || '10';
    let searchRadius = parseInt(radiusInKm) * 1000;

    directionsService.route({
        origin: startAddr,
        destination: endAddr,
        travelMode: google.maps.TravelMode[selectedMode]
    }, function(response, status) {
        if (status === 'OK') {
            directionsRenderer.setDirections(response);
            const endPoint = response.routes[0].legs[0].end_location;
            showStreetView(endPoint);
            showRecommendations(endPoint, searchRadius);
        } else {
            window.alert('Directions request failed due to ' + status);
        }
    });
}

function showStreetView(location) {
    pano.setPosition(location);
    pano.setVisible(true);
    map.setStreetView(pano);
}

function showRecommendations(endPoint, searchRadius) {
    let request = {
        location: endPoint,
        radius: searchRadius,
        type: ['tourist_attraction']
    };

    placesService.nearbySearch(request, function(results, status) {
        if (status === google.maps.places.PlacesServiceStatus.OK) {
            let recommendationsList = document.getElementById('recommendations');
            recommendationsList.innerHTML = '';
            results.forEach(function(place) {
                let li = document.createElement('li');
                li.textContent = place.name;
                li.onclick = function() {
                    document.getElementById('start').value = document.getElementById('end').value;
                    document.getElementById('end').value = place.name;
                    planRoute();
                };
                recommendationsList.appendChild(li);
            });
        } else {
            recommendationsList.innerHTML = '<li>No recommendations found</li>';
        }
    });
}
