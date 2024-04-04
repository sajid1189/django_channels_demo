from django.contrib import admin
from django.urls import include, path
from demo_app import views

urlpatterns = [
    path("", views.index, name="index"),
    path("private/", views.private, name="index"),
    path("admin/", admin.site.urls),
]
