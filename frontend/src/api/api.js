import axios from 'axios';

// Define the base API URL (optional, based on deployment environment)
const API_BASE_URL = process.env.REACT_APP_API_BASE_URL || '';

// Fetch star data for a specific exoplanet
export const fetchStarMapData = (ra, dec) => {
  return axios.get(`${API_BASE_URL}/api/starmap/${ra}/${dec}/`);
};
