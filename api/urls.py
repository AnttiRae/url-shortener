from django.contrib import admin
from django.urls import path
from .views import DecodeUrlView, EncodeUrlView

urlpatterns = [
    path('encode/', EncodeUrlView.as_view(), name='encode'),
    path('decode/', DecodeUrlView.as_view(), name='decode'),
]
