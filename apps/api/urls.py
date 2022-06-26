from django.urls import path

from .views import CityAPIView, StreetsInCityApiView, ShopAPIView

urlpatterns = [
    # get all cities
    path('city/', CityAPIView.as_view()),
    path('city/<int:city_id>/street/', StreetsInCityApiView.as_view()),
    path('shop/', ShopAPIView.as_view())

]
