from django.db import models
from django.db.models.fields import BooleanField
from django.contrib.auth.models import User

class todo(models.Model):
    job = models.CharField(max_length=28)
    stat = models.BooleanField(default=False)
    usrid = models.ForeignKey(User,on_delete=models.CASCADE)
    

    class Meta:
        ordering = ('stat',)

    def __str__(self):
        return self.job
