from django.urls import path
from .views import index, sent

urlpatterns = [
    path('', index, name='index'),
    path('sent/', sent, name='sent'),
]
