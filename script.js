//let map;
//let directionsService;
//let directionsRenderer;
//let autocompleteStart;
//let autocompleteEnd;
//let panorama;
//
//function initMapAndAutocomplete() {
//    map = new google.maps.Map(document.getElementById('map'), {
//        center: {lat: -34.397, lng: 150.644},
//        zoom: 8
//    });
//
//    directionsService = new google.maps.DirectionsService();
//    directionsRenderer = new google.maps.DirectionsRenderer();
//    directionsRenderer.setMap(map);
//
//    panorama = new google.maps.StreetViewPanorama(
//        document.getElementById('pano'), {
//            position: {lat: -34.397, lng: 150.644},
//            pov: {
//                heading: 34,
//                pitch: 10
//            }
//        });
//    map.setStreetView(panorama);
//
//    autocompleteStart = new google.maps.places.Autocomplete(
//        document.getElementById('start'),
//        { types: ['geocode'] }
//    );
//    autocompleteEnd = new google.maps.places.Autocomplete(
//        document.getElementById('end'),
//        { types: ['geocode'] }
//    );
//}
//
//function planRoute() {
//    let startAddr = document.getElementById('start').value;
//    let endAddr = document.getElementById('end').value;
//    let selectedMode = document.getElementById('mode').value;
//
//    directionsService.route({
//        origin: startAddr,
//        destination: endAddr,
//        travelMode: google.maps.TravelMode[selectedMode]
//    }, function(response, status) {
//        if (status === 'OK') {
//            directionsRenderer.setDirections(response);
//            const endPoint = response.routes[0].legs[0].end_location;
//            showStreetView(endPoint);
//        } else {
//            window.alert('Directions request failed due to ' + status);
//        }
//    });
//}
//
//
//function showStreetView(position) {
//    panorama.setPosition(position);
//    panorama.setVisible(true);
//}
//let map, pano, directionsRenderer, directionsService;
//
//function initMapAndAutocomplete() {
//    directionsRenderer = new google.maps.DirectionsRenderer();
//    directionsService = new google.maps.DirectionsService();
//
//    map = new google.maps.Map(document.getElementById('map'), {
//        center: { lat: -34.397, lng: 150.644 },
//        zoom: 6
//    });
//
//    pano = new google.maps.StreetViewPanorama(
//        document.getElementById('pano'), {
//            position: { lat: -34.397, lng: 150.644 },
//            pov: { heading: 34, pitch: 10 }
//        }
//    );
//
//    directionsRenderer.setMap(map);
//    directionsRenderer.setPanel(document.getElementById('right-panel'));
//
//    const control = document.getElementById('floating-panel');
//    control.style.display = 'block';
//    map.controls[google.maps.ControlPosition.TOP_CENTER].push(control);
//}
//
//function planRoute() {
//    let startAddr = document.getElementById('start').value;
//    let endAddr = document.getElementById('end').value;
//    let selectedMode = document.getElementById('mode').value;
//
//    directionsService.route({
//        origin: startAddr,
//        destination: endAddr,
//        travelMode: google.maps.TravelMode[selectedMode]
//    }, function(response, status) {
//        if (status === 'OK') {
//            directionsRenderer.setDirections(response);
//            const endPoint = response.routes[0].legs[0].end_location;
//            showStreetView(endPoint);
//        } else {
//            window.alert('Directions request failed due to ' + status);
//        }
//    });
//}
//
//function showStreetView(location) {
//    pano.setPosition(location);
//    pano.setPov({ heading: 34, pitch: 10 });
//}
//
//function useCurrentLocation() {
//    if (navigator.geolocation) {
//        navigator.geolocation.getCurrentPosition(function(position) {
//            let pos = {
//                lat: position.coords.latitude,
//                lng: position.coords.longitude
//            };
//
//            map.setCenter(pos);
//            pano.setPosition(pos);
//            document.getElementById('start').value = pos.lat + ',' + pos.lng;
//        }, function() {
//            handleLocationError(true, map.getCenter());
//        });
//    } else {
//        // Browser doesn't support Geolocation
//        handleLocationError(false, map.getCenter());
//    }
//}
//
//function handleLocationError(browserHasGeolocation, pos) {
//    window.alert(browserHasGeolocation ?
//                'Error: The Geolocation service failed.' :
//                'Error: Your browser doesn\'t support geolocation.');
//}
let map, pano, directionsRenderer, directionsService;

function initMapAndAutocomplete() {
    directionsRenderer = new google.maps.DirectionsRenderer();
    directionsService = new google.maps.DirectionsService();

    map = new google.maps.Map(document.getElementById('map'), {
        center: { lat: -34.397, lng: 150.644 },
        zoom: 6
    });

    pano = new google.maps.StreetViewPanorama(
        document.getElementById('pano'), {
            position: { lat: -34.397, lng: 150.644 },
            pov: { heading: 34, pitch: 10 }
        }
    );

    directionsRenderer.setMap(map);
    directionsRenderer.setPanel(document.getElementById('right-panel'));

    // 地址自动补全
    new google.maps.places.Autocomplete(document.getElementById('start'));
    new google.maps.places.Autocomplete(document.getElementById('end'));

    const control = document.getElementById('floating-panel');
    if (control) {
        control.style.display = 'block';
        map.controls[google.maps.ControlPosition.TOP_CENTER].push(control);
    }
}

function planRoute() {
    let startAddr = document.getElementById('start').value;
    let endAddr = document.getElementById('end').value;
    let selectedMode = document.getElementById('mode').value;

    directionsService.route({
        origin: startAddr,
        destination: endAddr,
        travelMode: google.maps.TravelMode[selectedMode]
    }, function(response, status) {
        if (status === 'OK') {
            directionsRenderer.setDirections(response);
            const endPoint = response.routes[0].legs[0].end_location;
            showStreetView(endPoint);
        } else {
            window.alert('Directions request failed due to ' + status);
        }
    });
}

function showStreetView(location) {
    pano.setPosition(location);
    pano.setPov({ heading: 34, pitch: 10 });
}

function useCurrentLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function(position) {
            let pos = {
                lat: position.coords.latitude,
                lng: position.coords.longitude
            };

            map.setCenter(pos);
            pano.setPosition(pos);
            document.getElementById('start').value = pos.lat + ',' + pos.lng;
        }, function() {
            handleLocationError(true, map.getCenter());
        });
    } else {
        // Browser doesn't support Geolocation
        handleLocationError(false, map.getCenter());
    }
}

function handleLocationError(browserHasGeolocation, pos) {
    window.alert(browserHasGeolocation ?
                'Error: The Geolocation service failed.' :
                'Error: Your browser doesn\'t support geolocation.');
}

