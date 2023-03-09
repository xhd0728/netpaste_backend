from django.db import models
from django.utils import timezone


# Create your models here.
class Text(models.Model):
    text = models.TextField()
    code_lang = models.CharField(max_length=32, default='text')
    create_time = models.DateTimeField(default=timezone.now)
