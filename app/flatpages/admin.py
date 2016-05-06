from django import forms
from django.contrib import admin

from ckeditor.widgets import CKEditorWidget

from .models import FlatPage


class FlatPageAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget)
    class Meta:
        model = FlatPage
        exclude = ['created']

class FlatPageAdmin(admin.ModelAdmin):
    form = FlatPageAdminForm
    list_display = ['title']

admin.site.register(FlatPage, FlatPageAdmin)
