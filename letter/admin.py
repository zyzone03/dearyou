from django.contrib import admin
from letter.models import *
# Register your models here.
class PostMember(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['title']
    
admin.site.register(Member)
admin.site.register(Letter)
admin.site.register(Contact)