
from django.contrib import admin
from django.urls import path
from form import views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('form/', views.form, name='form'),
]
