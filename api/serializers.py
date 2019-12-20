# Django Import
from rest_framework import serializers
from django.utils import timezone
# Project Import
from .models import Invitation


# Serializers define the API representation.
class InvitationSerializer(serializers.ModelSerializer):
    """
    Serializer to serialize/deserializer data.
    """
    id = serializers.CharField(read_only=True)
    createdTime = serializers.CharField(source='created_time', required=False)
    seconds = serializers.SerializerMethodField(read_only=True)
    creatorEmail = serializers.CharField(source='creator.email', read_only=True)
    creatorFullname = serializers.SerializerMethodField(read_only=True)

    @staticmethod
    def get_seconds(obj):
        return (timezone.now()-obj.created_time).total_seconds()

    @staticmethod
    def get_creatorFullname(obj):
        first_name = obj.creator.first_name
        last_name = obj.creator.last_name
        return first_name + ' ' + last_name

    class Meta:
        model = Invitation
        fields = ('id', 'createdTime', 'seconds', 'email', 'used', 'creatorEmail', 'creatorFullname')

    def update(self, instance, validated_data):
        """
        Update and return an existing Invitation instance, given the validated data.
        """
        instance.email = validated_data.get('email', instance.email)
        instance.used = validated_data.get('used', instance.used)
        instance.save()
        return instance
