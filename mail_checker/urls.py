
from django.contrib import admin
from django.urls import path, include
from form import views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('form/', views.form, name='form'),
    path('productkey/', views.productkey, name='productkey'),
    path('verify/', views.verify, name='verify'),
    path('accounts/', include('accounts.urls')),
]
