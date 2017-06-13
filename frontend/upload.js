import '../style/upload.scss';
import './header.js';
import './upload_form/file.js';
import './upload_form/submit.js';

function initMap(){
  let map = new google.maps.Map(document.getElementById('map'), {
    zoom: 3,
    center: {lat: -28.024, lng: 140.887}
  });

  setupListeners(map);
}

function setupListeners(map) {
  map.addListener('click', (e) => {
    document.querySelector('#lat-input').value = e.latLng.lat();
    document.querySelector('#lng-input').value = e.latLng.lng();
    console.log("LOCATION SET");
  });
}


window.initMap = initMap;
