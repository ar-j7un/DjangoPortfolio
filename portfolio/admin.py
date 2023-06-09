from django.contrib import admin
from .models import Portfolio
# Register your models here.
admin.site.register(Portfolio)


class PortfolioAdmin(admin.ModelAdmin):
    list_display=("name","college1","college2","place","dob","phone")