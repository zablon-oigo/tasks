from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    photo=models.ImageField(upload_to='users/%Y/%m/%d', default='avatar.jpg')
    date_joined=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self, *args,**kwargs):
        super().save(*args,**kwargs)

        # resize the image
        img=Image.open(self.photo.path)
        if img.height > 300 or img.width > 300:
            output_size=(300,200)
            # thumbnail
            img.thumbnail(output_size)
            img.save(self.photo.path)