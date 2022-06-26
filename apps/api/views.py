from datetime import datetime

from rest_framework.exceptions import NotFound
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .get_time import get_time_lists
from .models import City, Street, Shop
from .serializers import CitySerializer, StreetSerializer, ShopSerializer


class CityAPIView(ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class StreetsInCityApiView(ListAPIView):
    serializer_class = StreetSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        city_id = self.kwargs.get('city_id', None)

        if city_id is not None:
            queryset = Street.objects.filter(city_id=city_id)

            if queryset:
                return queryset
            else:
                raise NotFound


class ShopAPIView(ListCreateAPIView):
    serializer_class = ShopSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        request = self.request

        street = request.query_params.get('street')
        city = request.query_params.get('city')
        open_bool = request.query_params.get('open')

        time_now = datetime.utcnow().time().replace(microsecond=0)

        queryset = Shop.objects.all()

        if street:
            queryset = queryset.filter(shop_street__street_name=street)

        if city:
            queryset = queryset.filter(shop_street__city__city_name=city)

        if open_bool in ['1', '0']:

            time_open_values = queryset.values("time_open")
            time_close_values = queryset.values("time_close")

            if time_ranges := get_time_lists(open_bool, time_now, time_open_values, time_close_values):
                time_open_range, time_close_range = time_ranges
                queryset = queryset.filter(time_open__range=time_open_range).filter(time_close__range=time_close_range)
            else:
                raise NotFound

        return queryset
