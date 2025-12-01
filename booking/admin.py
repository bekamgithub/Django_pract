from django.contrib import admin
from .models import register,Booking

class BookingAdmin(admin.ModelAdmin):
    list_display = ("name", "service", "date", "time", "status")
    list_filter = ("service", "status", "date")
    search_fields = ("name", "email", "phone")
    ordering = ("date", "time")
    list_per_page = 20

admin.site.register(Booking,BookingAdmin)
admin.site.register(register)

# Register your models here.
