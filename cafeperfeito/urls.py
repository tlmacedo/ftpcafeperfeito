from django.urls import path

from cafeperfeito.views import LoginTemplateView, HomeTemplateView, ProdutosListView

app_name = 'cafeperfeito'

urlpatterns = [
    path('', LoginTemplateView.as_view(), name='login'),
    path('home/', HomeTemplateView.as_view(), name='home'),
    path('produtos/', ProdutosListView.as_view(), name='lista_produtos'),
    # path('empresa/', views.empresa, name='empresa'),
]
