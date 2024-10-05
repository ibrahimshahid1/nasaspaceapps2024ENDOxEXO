import numpy as np

def convert_ra_dec_to_cartesian(ra, dec, distance):
    ra_rad = np.radians(ra)
    dec_rad = np.radians(dec)
    x = distance * np.cos(dec_rad) * np.cos(ra_rad)
    y = distance * np.cos(dec_rad) * np.sin(ra_rad)
    z = distance * np.sin(dec_rad)
    return x, y, z

def translate_to_exoplanet(star_coords, exoplanet_coords):
    x_new = star_coords[0] - exoplanet_coords[0]
    y_new = star_coords[1] - exoplanet_coords[1]
    z_new = star_coords[2] - exoplanet_coords[2]
    return x_new, y_new, z_new

def convert_cartesian_to_ra_dec(x_new, y_new, z_new):
    ra_new = np.degrees(np.arctan2(y_new, x_new))
    dec_new = np.degrees(np.arcsin(z_new / np.sqrt(x_new**2 + y_new**2 + z_new**2)))
    if ra_new < 0:
        ra_new += 360
    return ra_new, dec_new

def calculate_star_positions_for_exoplanet(ra_exoplanet, dec_exoplanet, stars_data):
    distance_exoplanet = 1
    exoplanet_coords = convert_ra_dec_to_cartesian(ra_exoplanet, dec_exoplanet, distance_exoplanet)
    new_star_positions = []
    for star in stars_data:
        star_coords = convert_ra_dec_to_cartesian(star['ra'], star['dec'], star['distance'])
        x_new, y_new, z_new = translate_to_exoplanet(star_coords, exoplanet_coords)
        ra_new, dec_new = convert_cartesian_to_ra_dec(x_new, y_new, z_new)
        new_star_positions.append({'ra': ra_new, 'dec': dec_new})
    return new_star_positions
    