from rest_framework import viewsets
from rest_framework.response import Response

from drf_spectacular.utils import extend_schema

from drfecommerce.product.serializers import (CategorySerializer,ProductSerializer, BrandSerializer)
from drfecommerce.product.models import (Product, Category, Brand)

class BrandViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or users.

    """

    serializer_class = BrandSerializer

    @extend_schema(
        request=BrandSerializer,
        
    )
    def list(self, request):
        queryset = Brand.objects.all()
        serializer = BrandSerializer(queryset, many=True)
        return Response(serializer.data)

class CategoryViewSet(viewsets.ViewSet):
    serializer_class = CategorySerializer

    @extend_schema(
        request=CategorySerializer,
        
    )
    def list(self, request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)
    
class ProductViewSet(viewsets.ViewSet):
    serializer_class = ProductSerializer

    @extend_schema(
        request=ProductSerializer,
        
    )
    def list(self, request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)



