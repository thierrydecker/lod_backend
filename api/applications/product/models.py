import uuid

from django.db import models

from api.applications.workspace.models import Workspace


class Product(models.Model):
    id = models.UUIDField(
            primary_key=True,
            default=uuid.uuid4,
    )
    related_workspace = models.ForeignKey(
            Workspace,
            on_delete=models.PROTECT,
    )
    code = models.CharField(
            max_length=50,
    )
    description = models.CharField(
            max_length=150,
    )

    class Meta:
        db_table = 'products'
        unique_together = ('related_workspace', 'code',)
