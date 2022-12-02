import React, { useRef, useEffect, useState } from 'react';

import mapboxgl from '!mapbox-gl'; // eslint-disable-line import/no-webpack-loader-syntax
import MapboxGeocoder from '@mapbox/mapbox-gl-geocoder';
import "./MapboxView.css";

mapboxgl.accessToken = 'pk.eyJ1IjoiYXZhbmkxOCIsImEiOiJjbGI0amtmMnYwOHZuM3lsMHpreXZsZXU3In0.9F-GJGlYWjwdwTClH8xI2g';

export default function MapboxView() {

    const mapContainer = useRef(null);
    const map = useRef(null);
    //var marker = new mapboxgl.Marker();
    const [lng, setLng] = useState(-72.50187402113794);
    const [lat, setLat] = useState(42.37314021836991);
    const [zoom, setZoom] = useState(12);

    const srcMapboxGeocoder = new MapboxGeocoder({
        // Initialize the geocoder
        accessToken: mapboxgl.accessToken, // Set the access token
        mapboxgl: mapboxgl, // Set the mapbox-gl instance
        marker: false, // Do not use the default marker style
        placeholder: 'Search source in Amherst',
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
        placeholder: 'Search destination in Amherst',
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
            bounds.extend(srcMarker.getLngLat());
            bounds.extend(destMarker.getLngLat());
            map.current.fitBounds(bounds, {padding: 100});
          });

        destMapboxGeocoder.on('result', (event) => {
            console.log("dest", event.result);
            destMarker.setLngLat(event.result.geometry.coordinates).addTo(map.current);
            var bounds = new mapboxgl.LngLatBounds();
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
