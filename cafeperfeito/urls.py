from django.urls import path

from cafeperfeito.views import LoginTemplateView

app_name = 'cafeperfeito'

urlpatterns = [
    path('', LoginTemplateView.as_view(), name='login'),
]
