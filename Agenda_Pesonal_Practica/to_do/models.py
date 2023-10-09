from django.db import models
from datetime import date

class To_Do(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    date = models.DateField(default=date.today)
    estimated_end = models.DateField(blank=True, null=True)
    priority = models.IntegerField(default=3)
    filled = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    


