from django.db import models
from django.utils import timezone

# Create your models here.
class Delegate(models.Model):
    vote_frequency = models.CharField(max_length=100)
    tags = models.CharField(max_length=100)
    active_since = models.DateTimeField(default=timezone.now)