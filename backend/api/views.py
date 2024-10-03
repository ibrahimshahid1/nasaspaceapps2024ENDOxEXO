from astroquery.nasa_exoplanet_archive import NasaExoplanetArchive
from astroquery.ipac.nexsci.nasa_exoplanet_archive import NasaExoplanetArchive
from astroquery.gaia import Gaia
from astropy.coordinates import SkyCoord
import astropy.units as u
from django.http import JsonResponse

# Function to fetch exoplanets
def get_exoplanets(request):
    exoplanets = NasaExoplanetArchive.query_criteria(
        table="exoplanets",
        select="pl_name, hostname, ra, dec, pl_orbper, pl_rade, pl_masse, discoverymethod",
        where="pl_orbper > 0"
    )
    # Return the data as JSON
    return JsonResponse({'exoplanets': list(exoplanets)})

# Function to fetch stars from Gaia for a specific exoplanet
def get_star_data(request, ra, dec):
    # Use RA and Dec to get star data around the exoplanet's host star
    coord = SkyCoord(ra=float(ra)*u.deg, dec=float(dec)*u.deg, frame='icrs')
    
    gaia_query = f"""
        SELECT * FROM gaiadr2.gaia_source 
        WHERE CONTAINS(
            POINT('ICRS', ra, dec), 
            CIRCLE('ICRS', {coord.ra.deg}, {coord.dec.deg}, 0.01)) = 1
    """
    gaia_data = Gaia.launch_job(gaia_query).get_results()

    # Return the Gaia star data as JSON
    return JsonResponse({'stars': list(gaia_data)})

# Translate Star Position Data
import numpy as np

def convert_to_cartesian(ra, dec, distance):
    # Convert RA, Dec, and parallax (distance) to 3D Cartesian coordinates
    x = distance * np.cos(np.radians(dec)) * np.cos(np.radians(ra))
    y = distance * np.cos(np.radians(dec)) * np.sin(np.radians(ra))
    z = distance * np.sin(np.radians(dec))
    return x, y, z

def translate_to_exoplanet(star_coords, exoplanet_coords):
    # Translate star positions to exoplanet's viewpoint
    x_new = star_coords[0] - exoplanet_coords[0]
    y_new = star_coords[1] - exoplanet_coords[1]
    z_new = star_coords[2] - exoplanet_coords[2]
    return x_new, y_new, z_new

def convert_to_sky_coords(x, y, z):
    # Convert 3D Cartesian coordinates back to RA/Dec
    ra = np.degrees(np.arctan2(y, x))
    dec = np.degrees(np.arcsin(z / np.sqrt(x**2 + y**2 + z**2)))
    return ra, dec

