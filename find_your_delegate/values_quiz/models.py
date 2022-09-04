from django.db import models
from django.utils import timezone

# Create your models here.
class Delegate(models.Model):
    voting_freq = models.CharField(max_length=100)
    tag = models.CharField(max_length=100)
    active_since = models.DateTimeField(default=timezone.now)