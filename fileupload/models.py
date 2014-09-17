from django.db import models
from django.contrib.auth.models import User


class FileUpload(models.Model):
	docfile = models.FileField('File',upload_to='documents/%Y/%m/%d')
	acess = models.ManyToManyField(User)
	description = models.TextField(blank = True , null = True)
	date = models.DateTimeField(auto_now = True)

	def __unicode__(self):
		return self.description


