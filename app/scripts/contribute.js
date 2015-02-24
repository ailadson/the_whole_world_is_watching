//prevent default behavior when 'enter' is pressed. for search feature
window.addEventListener("keydown", function(evt){
    switch(evt.keyCode){
        case 13: evt.preventDefault();
    }
});

window.onload = function () {
    "use strict";
    WWWATCH.startContributeMap();
};

WWWATCH.startContributeMap = function () {
    "use strict";
    var map = new google.maps.Map(
        document.getElementById('mapContrib'),
        WWWATCH.getMapOptions({type : google.maps.MapTypeId.HYBRID})
    );
    
    var marker = WWWATCH.Marker.addMarker(
        map, 
        new google.maps.LatLng(40.477418, -98.441178), 
        { contrib : true }
    );
    
    //setup ui
    var input = document.getElementById('pac-input');
    var scrollDownBtn = document.getElementById('scroll-down');
    var mapInstruct = document.getElementById('mapIntruct');
    
    map.controls[google.maps.ControlPosition.TOP_LEFT].push(input);
    map.controls[google.maps.ControlPosition.BOTTOM_CENTER].push(scrollDownBtn);
    map.controls[google.maps.ControlPosition.TOP_CENTER].push(mapInstruct);
    
    var searchBox = new google.maps.places.SearchBox(input);
    
    google.maps.event.addListener(searchBox, 'places_changed', function() {
        var places = searchBox.getPlaces();
        
        if (places.length === 0) { return; }
        
        var bounds = new google.maps.LatLngBounds();
        
        for (var i = 0, place; place = places[i]; i++) {
            bounds.extend(place.geometry.location);
        }
        
        map.fitBounds(bounds);

        switch(places[0].types[0]){ //set zoom based on specificty of address
            case 'locality': 
                map.setZoom(13);
                break;
            case 'street_address' : 
                map.setZoom(20); 
                break;
            default : map.setZoom(13);
        }
        
    });
    
    
    google.maps.event.addListener(map, 'bounds_changed', function() {
        var bounds = map.getBounds();
        searchBox.setBounds(bounds);
    });
    
    google.maps.event.addListener(map, 'click', function(evt) {
        document.getElementById('lat').value = Math.round(evt.latLng.lat() * 10000000)/10000000;
        document.getElementById('lng').value = Math.round(evt.latLng.lng() * 10000000)/10000000;
        if(marker) {
            marker.setPosition(evt.latLng);
        } else {
            marker = PP.Marker.addMarker(map, evt.latLng, { contrib : true });
        }
    });
    
    google.maps.event.addListener(marker, 'dragend', function(evt) {
        document.getElementById('lat').value = Math.round(evt.latLng.lat() * 10000000)/10000000;
        document.getElementById('lng').value = Math.round(evt.latLng.lng() * 10000000)/10000000;
    });
    
};
