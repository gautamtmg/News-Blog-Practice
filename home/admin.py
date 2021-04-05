from django.contrib import admin
from .models import News, Slider

# Register your models here.

admin.site.register((News, Slider))