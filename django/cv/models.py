from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.

class ProgramImages(models.Model):
	text=models.CharField(max_length=100 , null=True)	
	image=models.FileField(null=True , blank=True)


	
	def __unicode__(self):
		return self.text