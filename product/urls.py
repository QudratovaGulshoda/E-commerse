from .views import *
from django.urls import path

urlpatterns = [
    path('product_list/', ProductListAPIView.as_view()),
    path('add_product/', ProductCreateAPIView.as_view()),
]
