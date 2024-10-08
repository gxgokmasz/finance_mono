from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.accounts.models import Account
from .models import User


@receiver(post_save, sender=User)
def create_user_account(sender, instance, created, **kwargs):
    if created:
        Account.objects.create(user=instance)
