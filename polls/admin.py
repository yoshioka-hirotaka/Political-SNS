from django.contrib import admin
from .models import Election, Vote
from politicians.models import Politician

class PoliticianInline(admin.TabularInline):
    model = Politician
    extra = 3

class ElectionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["election"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [PoliticianInline]
    list_display = ["election", "pub_date", "was_published_recently"]

class VoteAdmin(admin.ModelAdmin):
    list_display = ["user_name", "election", "vote", "pub_date", "was_published_recently"]

admin.site.register(Election, ElectionAdmin)
admin.site.register(Vote, VoteAdmin)