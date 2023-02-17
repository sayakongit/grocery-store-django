from django.urls import path
from .views import *

urlpatterns = [
    path('cart', CartView.as_view()),
    path('order', OrderView.as_view()),
]