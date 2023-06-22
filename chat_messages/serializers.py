from rest_framework import serializers
from .models import Message
from .models import ChatResponse


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = (
            "pk",
            "text",
            "response",
        )


class ChatResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatResponse
        fields = (
            "pk",
            "text",
        )
