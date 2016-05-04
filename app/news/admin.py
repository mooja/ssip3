from django import forms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget

from .models import NewsEntry


class NewsEntryAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget)
    class Meta:
        model = NewsEntry
        exclude = ['created']


class NewsEntryAdmin(admin.ModelAdmin):
    form = NewsEntryAdminForm
    list_display = ['title', 'created']

admin.site.register(NewsEntry, NewsEntryAdmin)
