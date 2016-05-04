from django.contrib import admin
from .models import Member

class MemberAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'email', 'homephone', 'cellphone']

admin.site.register(Member, MemberAdmin)
