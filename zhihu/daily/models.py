from django.db import models

# Create your models here.
class ZhDaily(models.Model):
	title = models.CharField(max_length=128)
	link = models.CharField(max_length=128)
	img = models.CharField(max_length=128)

	def __unicode__(self):
		return self.title