from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_time = models.DateField(auto_now_add=True)
    modified_time = models.DateField(auto_now=True)
    has_done = models.BooleanField(default=False)
    author = models.ForeignKey(User)

    class Meta:
        verbose_name = '事件 '
        verbose_name_plural = '事件'
        ordering = ['-created_time']