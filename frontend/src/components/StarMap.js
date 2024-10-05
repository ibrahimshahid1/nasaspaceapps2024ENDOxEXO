import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Canvas } from '@react-three/fiber';

function StarMap({ exoplanetRa, exoplanetDec }) {
  const [stars, setStars] = useState([]);

  // Fetch star data from the Django API when the exoplanet RA/Dec changes
  useEffect(() => {
    axios
      .get(`/api/starmap/${exoplanetRa}/${exoplanetDec}/`)
      .then((response) => {
        setStars(response.data);
      })
      .catch((error) => {
        console.error('Error fetching star positions:', error);
      });
  }, [exoplanetRa, exoplanetDec]);

  return (
    <Canvas>
      {stars.map((star, index) => (
        <mesh key={index} position={[star.ra, star.dec, 0]}>
          <sphereBufferGeometry args={[0.1, 32, 32]} />
          <meshBasicMaterial color="white" />
        </mesh>
      ))}
    </Canvas>
  );
}

export default StarMap;
