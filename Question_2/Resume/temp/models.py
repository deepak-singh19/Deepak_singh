from django.db import models

# Create your models here.
class Deepak(models.Model):

    phone = models.IntegerField()
    email = models.CharField(max_length=100, blank=False)
    firstname = models.CharField(max_length=100, blank=False)
    lastname = models.CharField(max_length=100, blank=False)
    role = models.IntegerField()
    username = models.CharField(max_length=100, blank=False)
    isActive = models.CharField(max_length=100, blank=False)
    _created_at = models.IntegerField()
    _uploaded_at = models.IntegerField()


    def __str__(self):
        return 'PHONE : {0} Email ; {1}'.format(self.phone, self.email)
