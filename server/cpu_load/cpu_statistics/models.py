from django.db import models
from django.utils import timezone


class CPULoad(models.Model):
    pub_date = models.DateTimeField(default=timezone.now)
    load = models.FloatField()

    class Meta:
        ordering = ['pub_date']

    def __str__(self):
        return f"{self.pub_date}: load - {self.load}%"
