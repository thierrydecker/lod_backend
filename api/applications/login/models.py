from django.contrib.auth.models import AbstractUser


class Login(AbstractUser):
    pass

    class Meta:
        db_table = 'logins'
