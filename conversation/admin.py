from django.contrib import admin

from .models import Conversation, CoversationMessage
# Register your models here.

admin.site.register(Conversation)
admin.site.register(CoversationMessage)