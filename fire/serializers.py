from rest_framework import serializers
from .models import Item,Client,Transaction

class itemsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Item
        fields='__all__'

class transactionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Transaction
        fields='__all__'