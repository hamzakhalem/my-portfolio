from django.contrib import admin
from django.urls import path, include
from .views import home
from django.conf.urls.i18n import i18n_patterns
urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('i18n', include('django.conf.urls.i18n')),
    path('en/', home, name="index"),
    path('fr/', home, name="index"),
    path('ar/', home, name="index"),
    path('ar/', home, name="index"),
]
