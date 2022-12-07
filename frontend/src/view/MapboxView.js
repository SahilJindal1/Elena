import React, { useRef, useEffect, useState } from 'react';

import mapboxgl from '!mapbox-gl'; // eslint-disable-line import/no-webpack-loader-syntax
import MapboxGeocoder from '@mapbox/mapbox-gl-geocoder';
import "./MapboxView.css";

mapboxgl.accessToken = 'pk.eyJ1IjoiYXZhbmkxOCIsImEiOiJjbGI0amtmMnYwOHZuM3lsMHpreXZsZXU3In0.9F-GJGlYWjwdwTClH8xI2g';
let map = null;

let src = null;
let dest = null;

export function MapboxView() {

    const mapContainer = useRef(null);
    map = useRef(null);
    //var marker = new mapboxgl.Marker();
    const [lng, setLng] = useState(-72.50187402113794);
    const [lat, setLat] = useState(42.37314021836991);
    const [zoom, setZoom] = useState(12);

    const srcMapboxGeocoder = new MapboxGeocoder({
        // Initialize the geocoder
        accessToken: mapboxgl.accessToken, // Set the access token
        mapboxgl: mapboxgl, // Set the mapbox-gl instance
        marker: false, // Do not use the default marker style
        placeholder: 'Search Source',
        proximity: {
            longitude: -72.50187402113794,
            latitude: 42.37314021836991
        }
      });

    const destMapboxGeocoder = new MapboxGeocoder({
        // Initialize the geocoder
        accessToken: mapboxgl.accessToken, // Set the access token
        mapboxgl: mapboxgl, // Set the mapbox-gl instance
        marker: false, // Do not use the default marker style
        placeholder: 'Search Destination',
        proximity: {
            longitude: -72.50187402113794,
            latitude: 42.37314021836991
        }
    });

    var srcMarker = new mapboxgl.Marker({color: "#005db2"});
    srcMarker.setLngLat([-72.5018, 42.3731]);

    var destMarker = new mapboxgl.Marker({color: "#dc143c"});
    destMarker.setLngLat([-72.5018, 42.3731]);

    useEffect(() => {
    if (map.current) return; // initialize map only once
    map.current = new mapboxgl.Map({
        container: mapContainer.current,
        style: 'mapbox://styles/mapbox/streets-v12',
        center: [lng, lat],
        zoom: zoom
    });
    
    map.current.addControl(srcMapboxGeocoder);
    map.current.addControl(destMapboxGeocoder);
    });

    useEffect(() => {
        if (!map.current) return;
        srcMapboxGeocoder.on('result', (event) => {
            console.log("src", event.result);
            srcMarker.setLngLat(event.result.geometry.coordinates).addTo(map.current);
            var bounds = new mapboxgl.LngLatBounds();
            src = event.result.geometry.coordinates;
            bounds.extend(srcMarker.getLngLat());
            bounds.extend(destMarker.getLngLat());
            map.current.fitBounds(bounds, {padding: 100});
          });

        destMapboxGeocoder.on('result', (event) => {
            console.log("dest", event.result);
            destMarker.setLngLat(event.result.geometry.coordinates).addTo(map.current);
            var bounds = new mapboxgl.LngLatBounds();
            dest = event.result.geometry.coordinates;
            bounds.extend(srcMarker.getLngLat());
            bounds.extend(destMarker.getLngLat());
            map.current.fitBounds(bounds, {padding: 100});
        });
    })

    useEffect(() => {
    if (!map.current) return; // wait for map to initialize
    map.current.on('move', () => {
        setLng(map.current.getCenter().lng.toFixed(4));
        setLat(map.current.getCenter().lat.toFixed(4));
        setZoom(map.current.getZoom().toFixed(2));
    });

    // map.current.on('click', (event) => {
    //     marker.setLngLat(event.lngLat).addTo(map.current);
    // });

    });

    return (
        
        <div className="mapView">
            <div className="sidebar">
                Longitude: {lng} | Latitude: {lat} | Zoom: {zoom}
            </div>
            <div ref={mapContainer} className="map-container" />
        </div>
        );
}

export function DisplayRoute(response) {

    // if (pathJSON == null || json.stringify(pathJSON) == {}) {
    //     //error
    //     return ""
    // }
    console.log("here")
    map.current.addSource('dijkstra-elevation-path', {
        type: 'geojson',
        data: {
            "type": "FeatureCollection",
            "features": [{
                "type": "Feature",
                "properties": {},
                "geometry": {
                    "type": "LineString",
                    coordinates: response['dijkstra']['path']
                    //"coordinates": [[-72.527381,42.351556],[-72.5260337,42.3515867],[-72.525857,42.351601],[-72.5257443,42.3516113],[-72.525012,42.351708],[-72.524353,42.351839],[-72.5221039,42.3541171],[-72.522022,42.354221],[-72.521744,42.3545731],[-72.5210113,42.3556561],[-72.5210566,42.3557675],[-72.5210408,42.3558147],[-72.5210161,42.3574905],[-72.5210083,42.3577576],[-72.5209888,42.3581485],[-72.5209708,42.3595563],[-72.5209696,42.3596156],[-72.5208019,42.3597326],[-72.520781,42.360697],[-72.520759,42.361988],[-72.520755,42.3626454],[-72.520754,42.362842],[-72.5207438,42.3632958],[-72.5205837,42.3647228],[-72.520462,42.365412],[-72.5201978,42.3671126],[-72.520181,42.36722],[-72.520172,42.367305],[-72.520053,42.368243],[-72.5198031,42.3682258],[-72.51919,42.369324],[-72.5190928,42.3700293],[-72.5171844,42.3702692],[-72.5175854,42.3706976],[-72.5175895,42.3710233]]}
            }}]
        }
    });

    console.log("added siurce")
    map.current.addLayer({
        'id': 'dijkstra-elevation-path-layer',
        'type': 'line',
        'source': 'dijkstra-elevation-path',
        'layout': {
            'line-join': 'round',
            'line-cap': 'round',
        },
        'paint': {
            'line-color': '#AFA925',
            'line-width': 5
        }
    });
    console.log("added layer")

    map.current.addSource('astar-elevation-path', {
        type: 'geojson',
        data: {
            "type": "FeatureCollection",
            "features": [{
                "type": "Feature",
                "properties": {},
                "geometry": {
                    "type": "LineString",
                    coordinates: response['a_star']['path']
                    //"coordinates": [[-72.527381,42.351556],[-72.5260337,42.3515867],[-72.5260404,42.3516593],[-72.5257548,42.3516821],[-72.5222176,42.3541703],[-72.522159,42.3542445],[-72.521744,42.3545731],[-72.5210113,42.3556561],[-72.5210566,42.3557675],[-72.5210408,42.3558147],[-72.5210161,42.3574905],[-72.5210083,42.3577576],[-72.5209888,42.3581485],[-72.5209708,42.3595563],[-72.5209696,42.3596156],[-72.5209524,42.3606794],[-72.5208856,42.3619662],[-72.520866,42.36264],[-72.5209103,42.3628323],[-72.5208976,42.3632934],[-72.5207342,42.3646983],[-72.5206533,42.3653703],[-72.520423,42.367325],[-72.5203196,42.368261],[-72.520139,42.3697067],[-72.5200246,42.370616],[-72.5198187,42.3705396],[-72.5187117,42.3708474],[-72.5186133,42.3708495],[-72.5175019,42.3703036],[-72.5175854,42.3706976],[-72.5175895,42.3710233]]}
            }}]
        }
    });

    console.log("added siurce")
    map.current.addLayer({
        'id': 'astar-elevation-path-layer',
        'type': 'line',
        'source': 'astar-elevation-path',
        'layout': {
            'line-join': 'round',
            'line-cap': 'round',
        },
        'paint': {
            'line-color': '#55AF25',
            'line-width': 5
        }
    });

    map.current.addSource('shortest-path', {
        type: 'geojson',
        data: {
            "type": "FeatureCollection",
            "features": [{
                "type": "Feature",
                "properties": {},
                "geometry": {
                    "type": "LineString",
                    coordinates: response['shortest_path']['path']
                    //"coordinates": [[-72.527381, 41.351556],[-72.5260337, 41.3515867],[-72.525857, 41.351601]]}
            }}]
        }
    });

    console.log("added siurce")
    map.current.addLayer({
        'id': 'shortest-path-layer',
        'type': 'line',
        'source': 'shortest-path',
        'layout': {
            'line-join': 'round',
            'line-cap': 'round',
        },
        'paint': {
            'line-color': '#253AAF',
            'line-width': 5
        }
    });
}

export {src, dest};
