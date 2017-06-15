let latInput = document.querySelector('#lat-input');
let lngInput = document.querySelector('#lng-input');
let input = document.querySelector('#pac-input');

let map;
let marker;

export function initMap() {
  map = new google.maps.Map(document.getElementById('map'), {
    zoom: 3,
    center: {lat: -28.024, lng: 140.887}
  });

  marker = new google.maps.Marker({
    map: map
  });

  let searchBox = new google.maps.places.SearchBox(input);
  map.controls[google.maps.ControlPosition.TOP_LEFT].push(input);

  // Bias the SearchBox results towards current map's viewport.
  map.addListener('bounds_changed', function() {
    searchBox.setBounds(map.getBounds());
  });

  searchBox.addListener('places_changed', function() {
    var places = searchBox.getPlaces();

    if (places.length == 0) return;

    latInput.value = places[0].geometry.location.lat();
    lngInput.value = places[0].geometry.location.lng();
  });

  setupMapListeners();
}

export function setupMapListeners() {
  map.addListener('click', (e) => {
    let latlng = { lat : e.latLng.lat(), lng : e.latLng.lng() };
    latInput.value = latlng.lat;
    lngInput.value = latlng.lng;
    if(marker) marker.setPosition(latlng);
  });
}
