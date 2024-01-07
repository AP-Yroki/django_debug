from django.contrib import admin
from .models import *
from .models import Manufacturer, Category, Product, Order

# Register your models here.
admin.site.register(Manufacturer)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)

class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'task', 'data', 'status')
    list_display_links = ('id', 'task')
    search_fields = ('task', )

admin.site.register(Todo, TodoAdmin)


