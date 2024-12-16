from rest_framework import serializers


class MenuCategoriesSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)
    description = serializers.CharField()


class MenuSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)
    description = serializers.CharField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    preparation_time = serializers.IntegerField()
    available = serializers.BooleanField()
    image_url = serializers.URLField()
    restaurants_id = serializers.IntegerField()
