from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from .models import User,Userprofile
    
@receiver(post_save,sender=User)
def post_save_create_profile_reciever(sender,instance,created,**kwargs):
     if created:
          Userprofile.objects.get_or_create(user=instance)
          print("User Profile is created")
     else:
          Userprofile.objects.get_or_create(user=instance)
          print('User is updated')
    

@receiver(pre_save,sender=User)
def pre_save_profile_receiver(sender,instance,**kwargs):
     print(instance.username,'this user is being  saved')
# post_save.connect(post_save_create_profile_reciever,sender=User)




