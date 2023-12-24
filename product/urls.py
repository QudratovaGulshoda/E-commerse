from django.urls import path
from .views import ProductListAPIView, ProductCreateAPIView, ProductUpdateAPIView, ProductDeleteAPIView,HomePageView

urlpatterns = [
    path('products/', ProductListAPIView.as_view(), name='product-list'),
    path('products/create/', ProductCreateAPIView.as_view(), name='product-create'),
    path('products/<int:pk>/update/', ProductUpdateAPIView.as_view(), name='product-update'),
    path('products/<int:pk>/delete/', ProductDeleteAPIView.as_view(), name='product-delete'),
    path('', HomePageView.as_view(), name='home'),
]
