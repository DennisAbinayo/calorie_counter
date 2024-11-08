from django.contrib import admin
from .models import FoodItem
# Register your models here.
@admin.register(FoodItem)
class FoodItemAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'calories', 'date_posted')
    list_filter = ('date_posted','calories', 'name')
    search_fields = ('name', 'calories')
    