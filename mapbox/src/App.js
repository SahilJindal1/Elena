import React, { useRef, useEffect, useState } from 'react';

import mapboxgl from '!mapbox-gl'; // eslint-disable-line import/no-webpack-loader-syntax
//import mbxGeocoding from '@mapbox/mapbox-sdk/services/geocoding';


mapboxgl.accessToken = 'pk.eyJ1IjoiYXZhbmkxOCIsImEiOiJjbGI0amtmMnYwOHZuM3lsMHpreXZsZXU3In0.9F-GJGlYWjwdwTClH8xI2g';

export default function App() {

    const mapContainer = useRef(null);
    const map = useRef(null);
    var marker = new mapboxgl.Marker();
    const [lng, setLng] = useState(-72.50187402113794);
    const [lat, setLat] = useState(42.37314021836991);
    const [zoom, setZoom] = useState(12);

    useEffect(() => {
    if (map.current) return; // initialize map only once
    map.current = new mapboxgl.Map({
        container: mapContainer.current,
        style: 'mapbox://styles/mapbox/streets-v12',
        center: [lng, lat],
        zoom: zoom
    });
    });

    useEffect(() => {
    if (!map.current) return; // wait for map to initialize
    map.current.on('move', () => {
        setLng(map.current.getCenter().lng.toFixed(4));
        setLat(map.current.getCenter().lat.toFixed(4));
        setZoom(map.current.getZoom().toFixed(2));
        console.log("longitude", lng);
        console.log("latitude", lat);
        console.log("zoom", zoom);
    });

    map.current.on('click', (event) => {
        marker.setLngLat(event.lngLat).addTo(map.current);
    });

    });

    return (
        <div>
            <div className="sidebar">
                Longitude: {lng} | Latitude: {lat} | Zoom: {zoom}
            </div>
            <div ref={mapContainer} className="map-container" />
        </div>
        );
}




