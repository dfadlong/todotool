from __future__ import unicode_literals

from django.db import models

import datetime

# Create your models here.

class Item(models.Model):
	text = models.TextField()
	created = models.DateField()
	isFinished = models.BooleanField()
	finished = models.DateField()
