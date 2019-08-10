from rest_framework import viewsets
from .models import Order,Product
from .serializers import OrderSerializer,ProductSerializer

class ProductView (viewsets.ModelViewSet):
    queryset=Order.objects.all()
    serializer_class=OrderSerializer

class OrderView (viewsets.ModelViewSet):
    queryset=Order.objects.all()
    serializer_class=OrderSerializer