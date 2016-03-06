from django.contrib import admin

from .models import Activity, ActivityFlow
# Register your models here.

class ActivityFlowInline(admin.TabularInline):
    model = ActivityFlow


class ActivityAdmin(admin.ModelAdmin):
    list_display = ('title',)
    inlines = [
        ActivityFlowInline
    ]

admin.site.register(Activity, ActivityAdmin)
