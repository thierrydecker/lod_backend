from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Login
from ..workspace.models import Workspace


@receiver(post_save, sender=Login)
def logins_post_save_handler(instance, created, **kwargs):
    if created:
        print("We have to create a new workspace for", instance.username, instance.pk)
        w = Workspace(
                description=f'Workspace created for user {instance.username}',
                related_login_id=instance.pk,
        )
        w.save()
        print("We created a new workspace for", instance.username, instance.pk)


def loaded():
    #
    # Dummy function called from apps
    #
    pass
