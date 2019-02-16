from olxapp.models import Category, Product
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import *
from rest_framework import generics


class AllViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A viewset for viewing all products
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryViewSet(generics.ListAPIView):
    """
    A viewset for viewing all products on basis of category
    """
    serializer_class = ProductSerializer

    def get_queryset(self):
        category = Category.objects.get(name=self.kwargs['category'])
        return Product.objects.filter(category=category)


class ProductDetailViewSet(generics.ListAPIView):
    """
    A viewset to view a single product
    """
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.filter(pk=self.kwargs['pk'])
    