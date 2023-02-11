from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        # fields = '__all__'
        exclude = ['slug']
        
class QuantityVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuantityVariant
        fields = '__all__'

class SizeVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = SizeVariant
        fields = '__all__'

class ColorVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColorVariant
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    quantity_type = QuantityVariantSerializer()
    color_type = ColorVariantSerializer()
    size_type = SizeVariantSerializer()
    category = CategorySerializer()
    class Meta:
        model = Product
        fields = '__all__'