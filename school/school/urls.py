"""
URL configuration for school project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from drf_spectacular.views import SpectacularAPIView
from drf_spectacular.views import SpectacularRedocView
from drf_spectacular.views import SpectacularSwaggerView
from school_modules.classes.urls import urlpatterns as classes_urls
from school_modules.pupils.urls import urlpatterns as pupils_urls
from school_modules.schools.urls import urlpatterns as schools_urls
from school_modules.workers.urls import urlpatterns as workers_urls

from school.settings import REGULAR_API_PREFIX

urlpatterns = [
    path("admin/", admin.site.urls),
    *workers_urls,
    *schools_urls,
    *classes_urls,
    *pupils_urls,
    path(f"{REGULAR_API_PREFIX}schema/", SpectacularAPIView.as_view(), name="schema"),
    # Optional UI:
    path(
        f"{REGULAR_API_PREFIX}docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        f"{REGULAR_API_PREFIX}docs/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]
