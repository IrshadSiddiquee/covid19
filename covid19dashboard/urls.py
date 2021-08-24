from django.urls import path
from covid19dashboard import views

urlpatterns = [
    path('', views.index),
]
