from django.urls import path

from ftp_v201.views import *

app_name = 'ftp_v201'

urlpatterns = [
    path('', LoginTemplateView.as_view(), name='login'),
]
