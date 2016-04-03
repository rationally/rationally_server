from django.db import models
from django.utils import timezone


class Topic(models.Model):
    TOPIC_STATE = (
        ('PROPOSED', 'Proposed'),
        ('IN INVESTIGATION', 'In Investigation'),
        ('DECIDED', 'Decided'),
        ('DISCARDED', 'Discarded'),
        ('ON HOLD', 'On Hold'),
    )

    name = models.CharField(max_length=200)
    state = models.CharField(max_length=20, choices=TOPIC_STATE, default=TOPIC_STATE[0])
    description = models.TextField(default='')
    date_modified = models.DateTimeField('date modified')
    date_created = models.DateTimeField('date created', default=timezone.now)
    #changelog

    def __str__(self):
        return self.name


class Alternative(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
