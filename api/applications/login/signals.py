from django.db.models.signals import post_delete
from django.db.models.signals import post_save
from django.db.models.signals import pre_delete
from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import Login


@receiver(pre_save, sender=Login)
def logins_pre_save_handler(instance, **kwargs):
    print("------------> A login is about to be saved")


@receiver(post_save, sender=Login)
def logins_post_save_handler(**kwargs):
    print("------------> A login has been saved")


@receiver(pre_delete, sender=Login)
def logins_pre_delete_handler(**kwargs):
    print("------------> A login is about to be deleted")


@receiver(post_delete, sender=Login)
def logins_post_delete_handler(**kwargs):
    print("------------> A login has been deleted")


def loaded():
    #
    # Dummy function called from apps
    #
    pass
