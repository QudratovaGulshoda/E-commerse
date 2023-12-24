from django.urls import path
from .views import *
urlpatterns = [
    path('list/',UserListAPIView.as_view()),
    path('add/',UserCreateAPIView.as_view()),
]
