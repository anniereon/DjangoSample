from django.urls import path
from .views import hello_view, result_view

urlpatterns = [
    path('', hello_view, name='hello'),
    path('result/', result_view, name='result'),
]
