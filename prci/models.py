from django.db import models

# Create your models here.


class Publisher(models.Model):
    pub_name = models.CharField(max_length=50, null=False, blank=False)
    pub_address = models.CharField(max_length=50, null=False, blank=False)
    is_published = models.BooleanField(default=False)
