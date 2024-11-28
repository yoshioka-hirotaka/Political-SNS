from django.contrib import admin

from .models import Face

class FaceAdmin(admin.ModelAdmin):
    list_display = ["user_name", "pub_date", "was_published_recently"]

admin.site.register(Face, FaceAdmin)