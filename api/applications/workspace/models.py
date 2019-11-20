import uuid

from django.db import models

from api.applications.login.models import Login


class Workspace(models.Model):
    id = models.UUIDField(
            primary_key=True,
            default=uuid.uuid4(),
    )
    related_login = models.ForeignKey(
            Login,
            on_delete=models.CASCADE,
    )
    description = models.CharField(
            max_length=30,
    )

    class Meta:
        db_table = 'workspaces'
