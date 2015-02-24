//namespace
var WWWATCH = {};


WWWATCH.currentPosition = undefined;

//returns opts object that's passed into goog maps
WWWATCH.getMapOptions = function (configur) {
    "use strict";
    var config = configur || {};
    
    return {
        center: config.latlng || new google.maps.LatLng(40.477418, -98.441178),
        zoom: config.zoom || 4,
        mapTypeId: config.type || google.maps.MapTypeId.HYBRID,
        streetViewControl: false,
        mapTypeControlOptions : {
            position: google.maps.ControlPosition.BOTTOM_LEFT
        }
    };
};


//MAP STUFF
WWWATCH.loadMap = function () {
    "use strict";
    var map = new google.maps.Map(
        document.getElementById('map-canvas'),
        WWWATCH.getMapOpts()
    );
};

WWWATCH.setCurrentPosition = function(position){
    "use strict";
    var lat = position.coords.latitude;
    var lng = position.coords.longitude;
    WWWATCH.currentPosition = new google.maps.LatLng(lat, lng);
    WWWATCH.startMap(WWWATCH.RecordManager);
};

WWWATCH.startMap = function (recordManager,opts) {
    "use strict";
    var map = new google.maps.Map(
        document.getElementById('map-canvas'),
        WWWATCH.getMapOptions({latlng : new google.maps.LatLng(opts.lat, opts.lng), 
                       zoom : opts.zoom })
    );
    
    //remove loading indicators
    document.body.style.cursor = "default";
    document.getElementById('loading').style.display = "none";
    
    //set up map UI
    var key = document.getElementById('keyBox');
    map.controls[google.maps.ControlPosition.RIGHT_BOTTOM].push(key);
    
    //add markers based on if these are search results or not
    if(opts.results){
        recordManager.loadRecords(map, WWWATCH.Record.SEARCH, opts.results);
        WWWATCH.Marker.addMarkers(map,recordManager.getAllRecords());
    } else {
        recordManager.loadRecords(map, WWWATCH.Record.RANDOM);
        WWWATCH.Marker.addMarkers(map,recordManager.getRndRecords(30));
    }
    
};

//PP.startContribMap = function () {
//    "use strict";
//    var map = new google.maps.Map(document.getElementById('mapContrib'),
//        PP.getMapOpts({
//            type : google.maps.MapTypeId.HYBRID
//        })
//    );
//    var marker = PP.Marker.addMarker(map, new google.maps.LatLng(40.477418, -98.441178), 
//                                             { contrib : true });
//    
//    var input = document.getElementById('pac-input');
//    map.controls[google.maps.ControlPosition.TOP_LEFT].push(input);
//    
//    var searchBox = new google.maps.places.SearchBox(input);
//    
//    google.maps.event.addListener(searchBox, 'places_changed', function() {
//        var places = searchBox.getPlaces();
//        
//        if (places.length == 0) { return; }
//        
//        var bounds = new google.maps.LatLngBounds();
//        
//        for (var i = 0, place; place = places[i]; i++) {
//            bounds.extend(place.geometry.location);
//        }
//        
//        map.fitBounds(bounds);
//
//        switch(places[0].types[0]){
//            case 'locality': 
//                map.setZoom(13);
//                break;
//            case 'street_address' : 
//                map.setZoom(20); 
//                break;
//            default : map.setZoom(13);
//        }
//        
//    });
//    
//    
//    google.maps.event.addListener(map, 'bounds_changed', function() {
//        var bounds = map.getBounds();
//        searchBox.setBounds(bounds);
//    });
//    
//    google.maps.event.addListener(map, 'click', function(evt) {
//        document.getElementById('lat').value = Math.round(evt.latLng.lat() * 10000000)/10000000;
//        document.getElementById('lng').value = Math.round(evt.latLng.lng() * 10000000)/10000000;
//        if(marker) {
//            marker.setPosition(evt.latLng);
//        } else {
//            marker = PP.Marker.addMarker(map, evt.latLng, { contrib : true });
//        }
//    });
//    
//    google.maps.event.addListener(marker, 'dragend', function(evt) {
//        document.getElementById('lat').value = Math.round(evt.latLng.lat() * 10000000)/10000000;
//        document.getElementById('lng').value = Math.round(evt.latLng.lng() * 10000000)/10000000;
//    });
//    
//};


WWWATCH.resetMap = function (record) {
    "use strict";
    var config = {latlng : new google.maps.LatLng(record.lat,record.lng)};
    var map = new google.maps.Map(
        document.getElementById('map-canvas'),
        WWWATCH.getMapOpts(config)
    );

    WWWATCH.Marker.addMarker(map,config.latlng,record);
    
};




