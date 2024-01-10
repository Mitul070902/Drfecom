
from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from rest_framework import routers

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from drfecommerce.product.views import (ProductViewSet, CategoryViewSet, BrandViewSet)


router = routers.DefaultRouter()
router.register(r'brand', BrandViewSet,basename='brand')
router.register(r'category', CategoryViewSet,basename='category')
router.register(r'product', ProductViewSet,basename='product')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include((router.urls))),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
