import uuid

from django.db import models


class Parent(models.Model):
    id = models.UUIDField(
            primary_key=True,
            default=uuid.uuid4,
    )
    code = models.CharField(
            max_length=50,
            unique=True,
    )
    description = models.CharField(
            max_length=150,
    )

    class Meta:
        db_table = 'parents'


class Child(models.Model):
    id = models.UUIDField(
            primary_key=True,
            default=uuid.uuid4,
    )
    related_parent = models.ForeignKey(
            Parent,
            on_delete=models.CASCADE,
    )
    code = models.CharField(
            max_length=50,
            unique=True,
    )
    description = models.CharField(
            max_length=150,
    )

    class Meta:
        db_table = 'childrens'
