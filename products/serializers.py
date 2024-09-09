from rest_framework import Serializers
from.models import Product

class ProductSerializer(Serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

