from django.contrib import admin
from gallery.models import *

# Register your models here.
class PhotoInline(admin.StackedInline):
    model=Photo

class ItemAdmin(admin.ModelAdmin):
    inlines=[PhotoInline]
    list_display = ('name',)

admin.site.register(Item,ItemAdmin)
admin.site.register(Photo)

