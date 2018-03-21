from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ggg/', include('webapp.urls')),
    path('', include('personal.urls')),
]
