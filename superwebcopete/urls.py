
from django.contrib import admin
from django.urls import path
from core import views #este

urlpatterns = [
    path('', views.home, name='home'), #este
    path('admin/', admin.site.urls),
]
