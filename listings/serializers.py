from rest_framework import serializers
from .models import Ad, AdImage, Category

class AdImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdImage
        fields = ['id', 'image', 'order']

class AdSerializer(serializers.ModelSerializer):
    images = AdImageSerializer(many=True, read_only=True)
    seller_name = serializers.CharField(source='seller.username', read_only=True)

    class Meta:
        model = Ad
        fields = ['id','seller','seller_name','title','description','price','currency','category','wilaya','images','created_at','is_published']
        read_only_fields = ['seller','is_published','created_at']
