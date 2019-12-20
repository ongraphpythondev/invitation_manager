# Python Import
import uuid
# Django Import
from django.conf import settings
from django.utils import timezone
from django.db import models


# Create your models here.
class Invitation(models.Model):
    """
    Model to an invitation.
    """
    # Attributes
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    created_time = models.DateTimeField(default=timezone.now, db_index=True)
    email = models.EmailField()
    used = models.BooleanField(default=False)

    # Relations
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='created_invitations',
        on_delete=models.CASCADE, null=True, blank=True)

    # Helper function
    def __str__(self):
        return "Invitation to {}".format(self.email)
