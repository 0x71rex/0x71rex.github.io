from django.contrib import admin
from django.urls import path, include  # Import include to include app-specific URLs

urlpatterns = [
    path('admin/', admin.site.urls),  # The admin site URL
    path('', include('resume_app.urls')),  # Include app-specific URLs
]
