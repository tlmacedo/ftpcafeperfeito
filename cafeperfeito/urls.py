from django.urls import path

from cafeperfeito.views import LoginTemplateView, HomeTemplateView

app_name = 'cafeperfeito'

urlpatterns = [
    path('', LoginTemplateView.as_view(), name='login'),
    path('home/', HomeTemplateView.as_view(), name='home'),
    # path('produto/', views.produto, name='produto'),
    # path('empresa/', views.empresa, name='empresa'),
]
