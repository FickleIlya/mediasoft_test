from django.db import models


# City model
class City(models.Model):
    city_id = models.AutoField(primary_key=True)
    city_name = models.CharField(max_length=168)

    def __str__(self):
        return self.city_name


# Street model
class Street(models.Model):
    street_id = models.AutoField(primary_key=True)
    street_name = models.CharField(max_length=100)

    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.street_name


# Shop model
class Shop(models.Model):
    shop_id = models.AutoField(primary_key=True)
    shop_name = models.CharField(max_length=100)
    address_building = models.CharField(max_length=10)
    time_open = models.TimeField()
    time_close = models.TimeField()

    shop_street = models.ForeignKey(Street, on_delete=models.CASCADE)

    def __str__(self):
        return self.shop_name
