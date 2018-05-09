
from django.contrib import admin
from django.urls import path,include
from authapp import views

urlpatterns = [
    path('sign_up/',views.sign_up),
]
