from django.contrib import admin

from .models import NewsEntry

class NewsEntryAdmin(admin.ModelAdmin):
    list_display = ['created', 'title']

admin.site.register(NewsEntry, NewsEntryAdmin)
