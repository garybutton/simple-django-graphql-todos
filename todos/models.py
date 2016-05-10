from __future__ import unicode_literals

from django.db import models


class Todo(models.Model):

    title = models.CharField(max_length=200)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title
