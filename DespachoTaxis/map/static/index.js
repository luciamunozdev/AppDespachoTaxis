// Initialize and add the map
// Integración
function initMap() {

    //var lat;
    //var lng;
    window.taxis = new Map()
        // The location of Uluru
    const uluru = { lat: 40.416729, lng: -3.703339 };
    window.map = new google.maps.Map(document.getElementById("map"), {
        zoom: 11,
        center: uluru,
    });

    window.directionsService = new google.maps.DirectionsService();
    window.directionsRenderer = new google.maps.DirectionsRenderer();
    directionsRenderer.setMap(map);

    // calculateAndDisplayRoute(directionsService, directionsRenderer, "Puerta del Sol", "Intercambiador de Plaza Castilla");
    //setInterval(update_marker, 3000, marker)
    //setInterval(check_new_routes, 5000, directionsService)
    setInterval(check_taxis, 250)

}



function add_marker(id, dest, lat, lng) { //Por terminar
    //console.log("----------", id, dest, lat, lng)
    const content_info_w =
        '<div id="contentMap">' +
        "</div>" +
        '<h2><strong>Taxi n&uacute;mero ' + id + ' </strong></h2>' +
        '<div id="bodyContent">' +
        '<li>Con destino </li>' + dest +
        "</div>";

    const infowindow = new google.maps.InfoWindow({
        content: content_info_w,
    });

    const marker = new google.maps.Marker({
        position: { lat, lng },
        icon: taxi_icon,
        map: map,
        optimized: true,
    });

    marker.addListener("click", () => {
        infowindow.open({
            anchor: marker,
            map,
            shouldFocus: false,
        });
    });
    return marker
}



function check_taxis() {
    $.ajax({
        url: '/ajax/check_taxis/',
        dataType: 'json',
        type: 'GET',
        success: function(data) {
            $.each(data, function(propNum, propData) {
                //console.log("aaaaa", propData.id, propData.dest, propData.Lat, propData.Lng)
                marker_n = taxis.has(propData.id) ? taxis.get(propData.id)['marker'] : add_marker(propData.id, propData.dest, parseFloat(propData.Lat), parseFloat(propData.Lng))
                    //if (taxis.has(propData.id) && taxis.get(propData.id)["ocupado"] == 'no') { marker_n.setIcon(taxi_icon_blue) } else {
                taxis.set(propData.id, {
                    id: propData.id,
                    dest: propData.dest,
                    Lat: parseFloat(propData.Lat),
                    Lng: parseFloat(propData.Lng),
                    marker: marker_n,
                    ocupado: propData.ocupado
                })
                marker_n.setPosition(new google.maps.LatLng(parseFloat(propData.Lat), parseFloat(propData.Lng)));
                //}

            });
        }
    });
}



function check_new_routes(directionsService) {

    $.ajax({
        url: '/ajax/check_new_routes/',
        dataType: 'json',
        type: 'GET',
        success: function(data) {
            Object.keys(data.route[0]).length
            if (Object.keys(data.route[0]).length > 0) {
                get_route(directionsService, data.route[0][1].origin, data.route[0][1].dest)

                var keys = Object.keys(data.route[0]);
                console.log(data.route[0][keys[0]].origin)
            }
        }
    });
}


//De aquí para abajo está sin terminar de implementar


function get_route(directionsService, origin, destination) {
    var res = directionsService.route({
        origin: {
            query: origin,
        },
        destination: {
            query: destination,
        },
        travelMode: google.maps.TravelMode.DRIVING,
    })

    $.ajax({
        url: '/ajax/send_route/',
        dataType: 'json',
        type: 'POST',
        data: res.routes,
        success: function(data) {
            console.log("new route")
        }
    });



}



function calculateAndDisplayRoute(directionsService, directionsRenderer, origin, destination) {
    directionsService.route({
            origin: {
                query: origin,
            },
            destination: {
                query: destination,
            },
            travelMode: google.maps.TravelMode.DRIVING,
        })
        .then((response) => {
            directionsRenderer.setDirections(response);
        });


}