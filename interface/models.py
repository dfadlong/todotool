from __future__ import unicode_literals

from django.db import models

import datetime

# Create your models here.

class Item(models.Model):
	text = models.TextField()
	created = models.DateField()
	isFinished = models.BooleanField()
	finished = models.DateField()
	@property
	def displayDate(self):
		interval = datetime.date.today() - self.created
		if interval == datetime.timedelta(days = 0):
			return 'today'
		elif interval == datetime.timedelta(days = 1):
			return 'yesterday'
		elif interval < datetime.timedelta(days = 7):
			return 'this week'
		return str(self.created)









