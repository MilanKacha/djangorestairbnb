from django.contrib import admin

# Register your models here.

from .models import Property, Resarvation

admin.site.register(Property)
admin.site.register(Resarvation)
