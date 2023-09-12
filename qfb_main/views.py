from django.contrib import admin
from django.urls import path
from qfb_main import views  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('qfbmain/', views.home, name='qfbmain'),  
    path('', views.home, name='home'),  
]
