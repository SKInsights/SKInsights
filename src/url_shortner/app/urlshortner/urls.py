from django.urls import path
from .views import home, redirect, createShortURL

urlpatterns = [
    path('', home),
    path('<str:url>', redirect, name='redirect'),
    path('create/', createShortURL, name='create')
]