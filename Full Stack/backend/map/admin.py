from django.contrib import admin
from .models import List

# Register your models here.

class ListAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'purchased')


admin.site.register(List, ListAdmin)