from django.urls import path

from . import views

urlpatterns = [
    path('json', views.get, name='get'),
    path('', views.init, name='init'),
]