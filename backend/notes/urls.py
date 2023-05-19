from django.urls import path

from . import views

urlpatterns = [
    path('api/notes/', views.api_note),
]