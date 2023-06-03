from django.contrib import admin
from .models import Farm, Farmer, Venture
# Register your models here.

admin.site.register(Farmer)
admin.site.register(Farm)
admin.site.register(Venture)