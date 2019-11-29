import uuid

from django.db import models

from api.applications.login.models import Login


class Workspace(models.Model):
    id = models.UUIDField(
            primary_key=True,
            default=uuid.uuid4,
    )
    related_login = models.ForeignKey(
            Login,
            on_delete=models.PROTECT,
    )
    description = models.CharField(
            max_length=150,
    )

    def __str__(self):
        login = Login.objects.get(pk=self.related_login)
        return f'{login.username} ({self.description})'

    class Meta:
        db_table = 'workspaces'
