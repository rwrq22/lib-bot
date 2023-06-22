from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Message
from .models import ChatResponse
from .serializers import MessageSerializer
from .serializers import ChatResponseSerializer
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.exceptions import NotFound


class Messages(APIView):
    def get(self, request):
        all_messages = Message.objects.all()
        serializer = MessageSerializer(all_messages, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            new_message = serializer.save()
            return Response(MessageSerializer(new_message).data)

    def delete(self, request):
        all_messages = Message.objects.all()
        all_messages.delete()
        return Response(status=HTTP_204_NO_CONTENT)

    authentication_classes = []


class ChatResponses(APIView):
    def get(self, request):
        all_chat_responses = ChatResponse.objects.all()
        serializer = ChatResponseSerializer(all_chat_responses, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ChatResponseSerializer(data=request.data)
        if serializer.is_valid():
            new_response = serializer.save()
            return Response(ChatResponseSerializer(new_response).data)

    def delete(self, request):
        all_chat_responses = ChatResponse.objects.all()
        all_chat_responses.delete()
        return Response(status=HTTP_204_NO_CONTENT)
