from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Tweet(models.Model):
    name = models.CharField(max_length=50, default='MYNAME')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mytweet')
    tweet = models.TextField(max_length=200)
    photo = models.ImageField(upload_to='tweet_images/' , blank = True , null = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f'{self.user.username} - {self.tweet[:20]}'  