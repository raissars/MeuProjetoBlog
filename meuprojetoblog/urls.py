from django.contrib import admin
from django.urls import path, include  # inclua o include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/', include('pages.urls')),  # isso conecta as URLs do app pages
]
