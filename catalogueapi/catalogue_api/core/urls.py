"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi  # new
from drf_yasg.views import get_schema_view as swagger_get_schema_view  # new

# new
schema_view = swagger_get_schema_view(
    openapi.Info(
        title="Catalogue API",
        default_version='v1',
        description="API documentation of the Catalogue micro service.",
    ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),  # new => it is the url to access the swagger documentation of the whole API
    path('hotels/', include('hotels.urls')),  # new
    path('rooms/', include('rooms.urls')),  # new
    path('room-types/', include('room_types.urls')),  # new
    path('hotel-options/', include('hotel_options.urls')),  # new
]
