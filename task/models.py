from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
class Task(models.Model):
    Task_status=(
        ('Pending','Pending'),
        ('Completed','Completed'),
    )
    title=models.CharField(max_length=200)
    slug=models.SlugField(max_length=200,default='')
    body=models.TextField(blank=True)
    status=models.CharField(max_length=10,choices=Task_status, default='Pending')
    created_by=models.ForeignKey(User, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['created_at']
        indexes=[
            models.Index(fields=['created_at'],)

        ]
    
    def save(self,*args,**kwargs):
        self.slug=slugify(self.title)
        super().save(*args,**kwargs)

    def __str__(self):
        return f'{self.title}'
    
    def get_absolute_url(self):
        return reverse('detail', args=[self.id, self.slug])
