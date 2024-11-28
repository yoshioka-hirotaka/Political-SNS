from django.contrib import admin
from .models import Politician

class PoliticianAdmin(admin.ModelAdmin):
    list_display = ["Name", "votes", "pub_date", "was_published_recently"]

admin.site.register(Politician, PoliticianAdmin)