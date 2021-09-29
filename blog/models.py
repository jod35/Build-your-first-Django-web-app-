from django.db import models
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    created=models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.title[:50]


    def get_absolute_url(self):

        return reverse('post_detail', kwargs={'pk': self.pk})  