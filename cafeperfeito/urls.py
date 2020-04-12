from django.template.context_processors import static
from django.urls import path

from cafeperfeito.views import LoginTemplateView
from ftpcafeperfeito import settings

app_name = 'cafeperfeito'

urlpatterns = [
    path('', LoginTemplateView.as_view(), name='login'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
