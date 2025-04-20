from django.contrib import admin
from django.urls import path, include  # ✅ Make sure to import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('backend.urls')),  # ✅ Link your app's urls
]
