from django.contrib.auth.models import User
from farmersapp.models import Farmer, Venture, Farm
from django.dispatch import receiver
from django.db.models.signals import post_save,post_delete

@receiver(post_save,sender = User)
def createFarmer(sender,instance,created,**kwargs):
    if created:
        user = instance
        farmer = Farmer.objects.create(
            user = user,
            email = user.email
        )
@receiver(post_delete,sender = Farmer)
def deleteFarmer(sender,instance,**kwargs):
    user = instance.user
    user.delete()


