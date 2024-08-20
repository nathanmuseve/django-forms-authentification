from django.contrib import admin
from .models import Tour

# Register your models here.
class TourAdmin(admin.ModelAdmin):
  list_display = ('id', 'origin_country', 'destination_country')
admin.site.register(Tour, TourAdmin)