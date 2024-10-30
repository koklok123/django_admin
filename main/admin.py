from django.contrib import admin
from .models import Pomen

@admin.register(Pomen)
class PomenAdmin(admin.ModelAdmin):
    list_display = ['name', 'pomen', 'image']
