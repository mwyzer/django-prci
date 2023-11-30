from django.db import models

# Create your models here.


class Publisher(models.Model):
    pub_name = models.CharField(max_length=50, null=False, blank=False)
    pub_address = models.CharField(max_length=50, null=False, blank=False)
    is_publisher = models.BooleanField(default=False, null=True, blank=True)
    publisher_founding_date = models.DateField(null=True, blank=True)
    # pub_founding_date = models.DateField(null=True, blank=True)
