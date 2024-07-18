from goods.models import ProductMod
from rest_framework import serializers

class ProducRest(serializers.ModelSerializer):
    class Meta:
        model = ProductMod
        fields = '__all__'