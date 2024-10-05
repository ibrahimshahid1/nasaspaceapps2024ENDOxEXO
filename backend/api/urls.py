from django.urls import path, register_converter
from .converters import FloatConverter  # Import the converter class
from . import views  # Import your views
from .views import StarPositionView

# Register the FloatConverter
register_converter(FloatConverter, 'float')

# Define your URL pattern
urlpatterns = [
   path('starmap/<float:exoplanet_ra>/<float:exoplanet_dec>/', StarPositionView.as_view(), name='starmap'),
]
