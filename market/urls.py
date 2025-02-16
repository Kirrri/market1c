from django.urls import path
from .views import market

urlpatterns = [
    path('', market, name='market'),
]