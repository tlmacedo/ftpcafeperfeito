from django.urls import path

from cafeperfeito.views import LoginTemplateView, PrincipalTemplateView

app_name = 'cafeperfeito'

urlpatterns = [
    path('', LoginTemplateView.as_view(), name='login'),
    path('principal/', PrincipalTemplateView.as_view(), name='principal'),
    # path('produto/', views.produto, name='produto'),
    # path('empresa/', views.empresa, name='empresa'),
]
