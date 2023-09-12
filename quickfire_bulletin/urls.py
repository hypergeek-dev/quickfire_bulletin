from django.contrib import admin
from django.urls import path
from qfb_main import views  # Make sure to import views from your app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('test/', views.test_page, name='test_page'),
]
