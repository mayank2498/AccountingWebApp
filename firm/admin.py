from django.contrib import admin
from .models import Firm

# Register your models here.

class FirmAdmin(admin.ModelAdmin):
    list_display = ["name", "year"]

admin.site.register(Firm,FirmAdmin)