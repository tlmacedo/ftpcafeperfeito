from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from cafeperfeito import views

urlpatterns = [
                  url(r'^$', views.index, name='index'),
                  # url(r'^login/$', views.login, name='login'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
