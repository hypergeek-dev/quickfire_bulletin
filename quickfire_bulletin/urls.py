from django.contrib import admin  # Import the admin module
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),  # Add this line for the admin interface
    path("", views.PostList.as_view(), name="home"),
]
