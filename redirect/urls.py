from django.urls import path
from .views import RequestRedirectView

urlpatterns = [
    path('<str:url_hash>/', RequestRedirectView.as_view(), name='redirect'),
]
