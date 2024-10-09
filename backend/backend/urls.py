from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView  # Import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),

    # Serve the React frontend for all other URLs
    re_path(r'^.*$', TemplateView.as_view(template_name='index.html')),
]
