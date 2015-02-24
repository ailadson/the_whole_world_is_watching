WWWATCH.Marker = {};
WWWATCH.Marker.CONTRIB = 2;


WWWATCH.Marker.addMarkers = function (map, recordArray) {
    "use strict";
    for (var i = 0; i < recordArray.length; i += 1){
        var record = recordArray[i];
        var latlng = new google.maps.LatLng(record.lat, record.lng);
        WWWATCH.Marker.addMarker(map,latlng,record);
    }
};

WWWATCH.Marker.addMarker = function (map, latlng, record) {
    "use strict";
    //get title and button image
    var title = WWWATCH.Marker.getMarkerTitle(record); 
    var drag = false;
    var path;
    
    //decide image (and dragable)
    if(record.fatal === 1){
        path = 'imgs/fatalMarker.png';
    } else if(record.brutal === 1){
        path = 'imgs/brutalMarker.png';
    } else if(record.wrongful === 1){
        path = 'imgs/wrongfulMarker.png';
    } else if(record.contrib){
        drag = true;
    } else {
        path = 'imgs/defaultMarker.png'; //other interactions
    }
    
    //create marker
    var marker = new google.maps.Marker({
        position: latlng,
        map: map,
        title: title,
        icon : path,
        draggable : drag
    });
    
    //mouse over effect for marker image
    if(!record.contrib){
        google.maps.event.addListener(marker, "mouseover", function(){
            marker.setIcon('imgs/h_'+path.split('/')[1]);
        });

        google.maps.event.addListener(marker, "mouseout", function(){
            marker.setIcon('imgs/'+path.split('/')[1]);
        });
    }
    
    google.maps.event.addListener(marker, "click", function(){
        map.setCenter(marker.getPosition());
        map.setZoom(22);
        WWWATCH.Video.startVideo(record);
    });
    
    WWWATCH.Marker.createInfoWindowListeners(map, marker, record);
    
    return marker; 
};


WWWATCH.Marker.createInfoWindowListeners = function (map,marker,record){
    "use strict";
    if(!record.getHTMLString) { return; }
    
    //create info window
    var contentString = record.getHTMLString();
    
    if (contentString) {
        var infowindow = new google.maps.InfoWindow({
            content: contentString
        });

        google.maps.event.addListener(marker, 'mouseover', function() {
            infowindow.open(map,marker);
        });
        
        google.maps.event.addListener(marker, 'mouseout', function() {
            infowindow.close();
        });
    }
};

WWWATCH.Marker.getMarkerTitle = function (config) {
    "use strict";
    var name = "";
    //add a space between first and last name
    if(config.firstName){
        name += config.firstName;
        if(config.lastName){
         name += (" " + config.lastName);
        }
    } else if(config.lastName){
         name += (config.lastName);
    }
    
    return name;
};