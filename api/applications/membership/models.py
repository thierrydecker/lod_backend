import uuid

from django.db import models

from api.applications.login.models import Login
from api.applications.workspace.models import Workspace


class Membership(models.Model):

    id = models.UUIDField(
            primary_key=True,
            default=uuid.uuid4,
    )
    related_login = models.ForeignKey(
            Login,
            on_delete=models.PROTECT,
    )
    related_workspace = models.ForeignKey(
            Workspace,
            on_delete=models.PROTECT,
    )

    class Meta:
        db_table = 'memberships'
        unique_together = ('related_login', 'related_workspace',)
