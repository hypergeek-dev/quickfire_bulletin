from django.contrib import admin
from django.urls import path, include  
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),  
    path("", views.PostList.as_view(), name="home"),
]
