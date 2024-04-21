from rest_framework import serializers
from ..models import Store

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        exclude = ['deleted']
        
    def create(self, validated_data):
        validated_data['customer'] = self.context['request'].user.customer
        return super().create(validated_data)
    
    