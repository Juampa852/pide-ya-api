from django.views.generic import TemplateView
from django.urls import path, include
from .views import HelloView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('hello/', HelloView.as_view(), name='Ejemplo'),
    path('token/', obtain_auth_token, name='API Token Auth'),
]