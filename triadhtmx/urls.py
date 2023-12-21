from django.contrib import admin
from django.urls import path, include
from triad.models import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('triad.urls')),
]
