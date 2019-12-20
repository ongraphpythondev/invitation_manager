# Django Imports
from django.http import Http404
from rest_framework import views
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# Project Imports
from .models import Invitation
from .serializers import InvitationSerializer
from .tasks import celery_mail_generation


class InvitationGetCreateView(views.APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    paginator = PageNumberPagination()
    """
    To get detail about an invitation and create new invitation
    """
    serializer_class = InvitationSerializer

    def get(self, request, *args, **kwargs):
        queryset = Invitation.objects.all().order_by('-created_time')
        paginated_response = self.serializer_class(
            self.paginator.paginate_queryset(queryset, request),
            many=True
        )
        return self.paginator.get_paginated_response(paginated_response.data)

    def post(self, request, *args, **kwargs):
        serialized_data = self.serializer_class(data=request.data)
        receiver = request.data.get('email')
        if serialized_data.is_valid(raise_exception=True):
            serialized_data.save(creator=request.user)
            celery_mail_generation.delay(receiver)
            return Response(serialized_data.data)


class InvitationRetrieveUpdateDeleteVIew(views.APIView):
    """
    For edit and delete an invitation
    """
    serializer_class = InvitationSerializer
    queryset = Invitation.objects.all()

    def get_object(self, pk):
        try:
            return Invitation.objects.get(pk=pk)
        except Invitation.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        invitation = self.get_object(pk)
        return Response(self.serializer_class(invitation).data)

    def patch(self, request, pk):
        instance = self.get_object(pk)
        email = request.data.get('email')
        serialized_data = self.serializer_class(instance=instance, data=request.data)
        if serialized_data.is_valid(raise_exception=True):
            if email and email != instance.email:
                celery_mail_generation.delay(email)
            updated_instance = serialized_data.update(instance=instance, validated_data=serialized_data.validated_data)
            return Response(updated_instance.id)

    def delete(self, request, pk):
        instance = self.get_object(pk)
        instance.delete()
        return Response(pk)
