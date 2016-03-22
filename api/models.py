import datetime
from django.db import models
from django.utils import timezone


class Decision(models.Model):
    name = models.CharField(max_length=200)
    modified_date = models.DateTimeField('date modified')

    def __str__(self):
        return self.name

    def was_modified_recently(self):
        return self.modified_date >= timezone.now() - datetime.timedelta(days=1)


class Alternative(models.Model):
    decision = models.ForeignKey(Decision, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
