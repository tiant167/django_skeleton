from django.contrib import admin
from .models import Order
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class OrderAdmin(ImportExportModelAdmin):
    list_display = ('recipe_num', 'source', 'amount')
    list_filter = ('source', 'amount')

admin.site.register(Order, OrderAdmin)
