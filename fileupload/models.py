from django.db import models
from django.contrib.auth.models import User


class FileUpload(models.Model):
	document = models.FileField(upload_to = 'documents/%Y/%m/%d')
	allowed_users = models.ManyToManyField(User)
	description = models.CharField(max_length = 100, blank = True, null = True)
	date_upload = models.DateTimeField(auto_now = True)
	adler32 = models.CharField(max_length = 256, blank = True, null = True)

	def __unicode__(self):
		return self.description


