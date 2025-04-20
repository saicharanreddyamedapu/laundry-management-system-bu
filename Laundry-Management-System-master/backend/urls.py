from django.urls import path
from . import views  # Import views from current folder

urlpatterns = [
    path('', views.home, name='home'),  # Show homepage
]
