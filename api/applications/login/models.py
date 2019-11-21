import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class Login(AbstractUser):
    id = models.UUIDField(
            primary_key=True,
            default=uuid.uuid4,
    )

    class Meta:
        db_table = 'logins'
