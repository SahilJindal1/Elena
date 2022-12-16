import React, { useRef, useEffect, useState } from 'react';

import mapboxgl from '!mapbox-gl'; // eslint-disable-line import/no-webpack-loader-syntax
import MapboxGeocoder from '@mapbox/mapbox-gl-geocoder';
import "./MapboxView.css";

mapboxgl.accessToken = 'pk.eyJ1IjoiYXZhbmkxOCIsImEiOiJjbGI0amtmMnYwOHZuM3lsMHpreXZsZXU3In0.9F-GJGlYWjwdwTClH8xI2g';
let map = null;

let src = null;
let dest = null;
var srcMarker;
var destMarker;
var srcMapboxGeocoder;
var destMapboxGeocoder;

export default function MapboxView() {

    const mapContainer = useRef(null);
    map = useRef(null);
    //var marker = new mapboxgl.Marker();
    const [lng, setLng] = useState(-72.50187402113794);
    const [lat, setLat] = useState(42.37314021836991);
    const [zoom, setZoom] = useState(12);
    const bounds = [-72.577934, 42.285930,  -72.455105, 42.443616];
    srcMapboxGeocoder = useRef(new MapboxGeocoder({
        // Initialize the geocoder
        accessToken: mapboxgl.accessToken, // Set the access token
        mapboxgl: mapboxgl, // Set the mapbox-gl instance
        marker: false, // Do not use the default marker style
        placeholder: 'Search Source',
        proximity: {
            longitude: -72.50187402113794,
            latitude: 42.37314021836991
        },
        bbox: bounds
      }));

    destMapboxGeocoder = useRef(new MapboxGeocoder({
        // Initialize the geocoder
        accessToken: mapboxgl.accessToken, // Set the access token
        mapboxgl: mapboxgl, // Set the mapbox-gl instance
        marker: false, // Do not use the default marker style
        placeholder: 'Search Destination',
        proximity: {
            longitude: -72.50187402113794,
            latitude: 42.37314021836991
        },
        bbox: bounds
    }));

    srcMarker = useRef(new mapboxgl.Marker({color: "#005db2"}));
    //srcMarker.current.setLngLat([-72.5018, 42.3731]);

    destMarker = useRef(new mapboxgl.Marker({color: "#dc143c"}));
    //destMarker.current.setLngLat([-72.5018, 42.3731]);

    useEffect(() => {
    if (map.current) return; // initialize map only once
    map.current = new mapboxgl.Map({
        container: mapContainer.current,
        style: 'mapbox://styles/mapbox/streets-v12',
        center: [lng, lat],
        zoom: 13
    });
    
    map.current.addControl(srcMapboxGeocoder.current, 'top-left');
    map.current.addControl(destMapboxGeocoder.current, 'top-left');
    map.current.addControl(new mapboxgl.NavigationControl(), 'bottom-right');
    });

    useEffect(() => {
        if (!map.current) return;
        srcMapboxGeocoder.current.on('result', (event) => {
            //console.log("src", event.result);
            srcMarker.current.setLngLat(event.result.geometry.coordinates).addTo(map.current);
            var bounds = new mapboxgl.LngLatBounds();
            src = event.result.geometry.coordinates;
            bounds.extend(srcMarker.current.getLngLat());
            bounds.extend(destMarker.current.getLngLat());
            map.current.fitBounds(bounds, {padding: 100});   
          });

        destMapboxGeocoder.current.on('result', (event) => {
            //console.log("dest", event.result);
            destMarker.current.setLngLat(event.result.geometry.coordinates).addTo(map.current);
            var bounds = new mapboxgl.LngLatBounds();
            dest = event.result.geometry.coordinates;
            bounds.extend(srcMarker.current.getLngLat());
            bounds.extend(destMarker.current.getLngLat());
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
    try{
        map.current.removeLayer("dijkstra-elevation-path-layer");
        map.current.removeSource("dijkstra-elevation-path");
        map.current.removeLayer("astar-elevation-path-layer");
        map.current.removeSource("astar-elevation-path");
        map.current.removeLayer("shortest-path-layer");
        map.current.removeSource("shortest-path");
    }
    catch{
        console.log("Error handled! No layers in first search");
    }
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


export function ResetMap() {
    console.log("resetting map");
    try{
        srcMapboxGeocoder.current.clear();
        srcMarker.current.remove();
        destMapboxGeocoder.current.clear();
        destMarker.current.remove();
        map.current.removeLayer("dijkstra-elevation-path-layer");
        map.current.removeSource("dijkstra-elevation-path");
        map.current.removeLayer("astar-elevation-path-layer");
        map.current.removeSource("astar-elevation-path");
        map.current.removeLayer("shortest-path-layer");
        map.current.removeSource("shortest-path");
    }
    catch(e) {
        console.log("Error handled! Layer is not added yet :)")
    }
}


export {src, dest};