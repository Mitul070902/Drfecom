from rest_framework import viewsets
from rest_framework.response import Response
from drfecommerce.product.serializers import (CategorySerializer,ProductSerializer, BrandSerializer)
from drfecommerce.product.models import (Product, Category, Brand)

class BrandViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or users.

    """
    def list(self, request):
        queryset = Brand.objects.all()
        serializer = BrandSerializer(queryset, many=True)
        return Response(serializer.data)

class CategoryViewSet(viewsets.ViewSet):
    
    def list(self, request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)
    
class ProductViewSet(viewsets.ViewSet):
   
    def list(self, request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)



