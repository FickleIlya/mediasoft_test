from django.contrib import admin

from .models import Shop, Street, City

admin.site.register(City)
admin.site.register(Shop)
admin.site.register(Street)
