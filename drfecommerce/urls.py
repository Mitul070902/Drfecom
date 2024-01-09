
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import routers
from drfecommerce.product.views import (ProductViewSet, CategoryViewSet, BrandViewSet)


router = routers.DefaultRouter()
router.register(r'brand', BrandViewSet,basename='brand')
router.register(r'category', CategoryViewSet,basename='category')
router.register(r'product', ProductViewSet,basename='product')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include((router.urls))),
]
