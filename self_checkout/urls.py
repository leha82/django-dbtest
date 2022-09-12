from django.urls import path
from self_checkout import views

urlpatterns = [
    path('', views.index),
    path('insert/', views.insert),
    path('search/', views.searchName, name='searchName'),
]
