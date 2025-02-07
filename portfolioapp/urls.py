from django.contrib import admin
from django.urls import path, include
from .views import home, homefr, homear
from django.conf.urls.i18n import i18n_patterns
urlpatterns = [
    path('/', home, name="index"),
    path('en/', home, name="index"),
    path('fr/', homefr, name="indexfr"),
    path('ar/', homear, name="indexar"),
    
]
