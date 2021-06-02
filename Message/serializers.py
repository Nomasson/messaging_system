from rest_framework import serializers
from .models import Message

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'receiver', 'sender', 'subject', 'message', 'creation_date', 'is_read')