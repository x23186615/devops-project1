from django.urls import path
from . import views

urlpatterns = [
    path('', views.chocolate_list, name='chocolate_list'),
    path('chocolate/<int:pk>/', views.chocolate_detail, name='chocolate_detail'),
]
