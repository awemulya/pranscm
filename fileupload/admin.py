from django.contrib import admin

from models import FileUpload

class FileUploadAdmin(admin.ModelAdmin):
		fieldsets = [
			('Select File To Upload',{'fields': ['docfile']}),
			('Description',{'fields': ['description']}),
			('Acess To',{'fields': ['acess']}),
			# ('Date information', {'fields': ['docfile'], 'classes': ['collapse']}),
		]
		list_display = ('docfile',  'description', 'date')
		list_filter= ('acess', 'date')
		search_fields = ['description','date']

admin.site.register(FileUpload, FileUploadAdmin)