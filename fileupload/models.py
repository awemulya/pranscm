from django.db import models
from django.contrib.auth.models import User
import os

class FileUpload(models.Model):
	filename = models.CharField(max_length = 256)
	uploaded_file_url= models.CharField(max_length = 256)
	allowed_users = models.ManyToManyField(User)
	description = models.CharField(max_length = 100, blank = True, null = True)
	uploaded_date = models.DateTimeField(auto_now = True, null=True)
	adler32 = models.CharField(max_length = 256, blank = True, null = True)
	is_deleted = models.BooleanField(default = False)

	def __unicode__(self):
		return self.uploaded_file_url


