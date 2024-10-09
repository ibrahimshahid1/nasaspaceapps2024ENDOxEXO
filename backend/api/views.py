from rest_framework.views import APIView
from rest_framework.response import Response
from astroquery.gaia import Gaia
from .utils import calculate_star_positions_for_exoplanet
from django.http import JsonResponse
from .utils import calculate_star_positions_for_exoplanet


class StarPositionView(APIView):
    def get(self, request, exoplanet_ra, exoplanet_dec):
        # Query the Gaia catalog for nearby stars
        job = Gaia.launch_job(f"SELECT TOP 10 source_id, ra, dec, parallax FROM gaiadr3.gaia_source WHERE "
                              f"ra BETWEEN {exoplanet_ra - 5} AND {exoplanet_ra + 5} AND "
                              f"dec BETWEEN {exoplanet_dec - 5} AND {exoplanet_dec + 5}")
        stars = job.get_results()

        # Prepare star data with their distances
        stars_data = [{'ra': star['ra'], 'dec': star['dec'], 'distance': 1 / (star['parallax'] * 0.001)} for star in stars]

        # Use the utility function to calculate new star positions
        new_star_positions = calculate_star_positions_for_exoplanet(exoplanet_ra, exoplanet_dec, stars_data)

        # Return the new positions as a response
        return Response(new_star_positions)
