from .models import *

@receiver(post_save, sender=User)
def create_user(sender, instance=None, created=False,  **kwargs):
    if created:
        print("New User have been created...", user=instance.username)
    print("User have updated data..!!")