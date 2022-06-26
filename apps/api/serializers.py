from rest_framework import serializers

from .models import Shop, Street, City


class StreetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Street
        fields = '__all__'

    def to_representation(self, instance):
        rep = super(StreetSerializer, self).to_representation(instance)
        rep['city'] = instance.city.city_name
        return rep


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class ShopSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shop
        fields = '__all__'

    def to_representation(self, instance):
        rep = super(ShopSerializer, self).to_representation(instance)
        rep['shop_street'] = instance.shop_street.street_name
        return rep
