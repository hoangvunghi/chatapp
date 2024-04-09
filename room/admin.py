from django.contrib import admin
from .models import Room, Message

admin.site.register(Room)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('room', 'user', 'content', 'date_added')
    list_filter = ('room', 'user', 'date_added')
    search_fields = ('content',)
admin.site.register(Message, MessageAdmin)
