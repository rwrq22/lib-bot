from django.contrib import admin
from .models import Message
from .models import ChatResponse


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    pass


@admin.register(ChatResponse)
class ChatResponseAdmin(admin.ModelAdmin):
    pass
