from blog.models import *
from django.dispatch import receiver
from django.db.models.signals import post_save

# @receiver(post_save,sender=Author)
@receiver(post_save)
def post_save_handler(sender,instance,**kwargs):
    print(sender.__class__)
    print(instance.__class__)
    print(isinstance(instance,(Article,Author)))
    print(kwargs)


print("signals imported----------------------------------")