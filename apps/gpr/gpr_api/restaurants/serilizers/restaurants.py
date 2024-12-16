from rest_framework import serializers


class RestaurantsCategoriesSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    description = serializers.CharField()


class RestaurantsSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)
    address = serializers.CharField()
    rating = serializers.FloatField()
    status = serializers.CharField(max_length=20)
    category = RestaurantsCategoriesSerializer()
    latitude = serializers.DecimalField(max_digits=21, decimal_places=11)
    longitude = serializers.DecimalField(max_digits=21, decimal_places=11)
