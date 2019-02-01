from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
from django.urls import path

from cafeperfeito import views

urlpatterns = [
    path('', views.index, name='index'),
    path('produto/', views.produto, name='produto'),
    path('empresa/', views.empresa, name='empresa'),
]
