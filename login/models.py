from django.db import models

# Create your models here.

class Detail(models.Model):
    application = models.CharField(max_length=200)
    component = models.CharField(max_length=200)
    latest_version = models.CharField(max_length=200)
    signoff_status = models.CharField(max_length=200)
    requester = models.CharField(max_length=200)


    def __str__(self):
        return self.application
