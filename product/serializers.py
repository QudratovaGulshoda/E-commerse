from rest_framework import serializers
from .models import *


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'photo',
            'price',
            'status',
            'created_at',
            'updated_at',
            'user'
        )
