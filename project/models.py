from django.db import models

# Create your models here.

class RequestForm(models.Model):
    timestamp = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=10)
    phone = models.CharField(max_length=11, blank=True, null=True)
    email = models.CharField(max_length=25, blank=True, null=True)
    start_date = models.CharField(max_length=8, blank=True, null=True)
    end_date = models.CharField(max_length=8, blank=True, null=True)
    datatype = models.CharField(max_length=10, blank=True, null=True)
    estimate_price = models.CharField(max_length=10, blank=True, null=True)
    real_price = models.CharField(max_length=10, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return '{} {}'.format(self.name, self.phone)
