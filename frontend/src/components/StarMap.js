import React, { useState, useEffect } from 'react';
import { Canvas } from '@react-three/fiber';
import axios from 'axios';
import { extend } from '@react-three/fiber';
import { SphereGeometry } from 'three';
extend({ SphereGeometry });

function StarMap({ exoplanetRa, exoplanetDec }) {
  const [stars, setStars] = useState([]);

  useEffect(() => {
    axios
      .get(`/api/starmap/${exoplanetRa}/${exoplanetDec}/`)
      .then(response => setStars(response.data))
      .catch(error => console.error('Error fetching star data:', error));
  }, [exoplanetRa, exoplanetDec]);

  return (
    <Canvas>
      {stars.map((star, index) => (
        <mesh key={index} position={[star.ra, star.dec, 0]}>
          {/* Use Sphere Geometry instead of SphereBufferGeometry */}
          <sphereGeometry args={[0.1, 32, 32]} />
          <meshBasicMaterial color="white" />
        </mesh>
      ))}
    </Canvas>
  );
}

export default StarMap;
