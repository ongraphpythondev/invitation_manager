# Django Imports
from django.conf.urls import url
# Project Imports
from .views import InvitationGetCreateView, InvitationRetrieveUpdateDeleteVIew


urlpatterns = [
    url(r'^invitations/$', InvitationGetCreateView.as_view()),
    url(r'^invitations/(?P<pk>[0-9a-f-]+)/$', InvitationRetrieveUpdateDeleteVIew.as_view())
]
