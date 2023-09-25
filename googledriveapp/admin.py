from django.contrib import admin
from googledriveapp.models import File, Folder, Details
# Register your models here.
@admin.register(Folder)
class Adminfolder(admin.ModelAdmin):
   list_display = ('foldername','folderuser')
   
@admin.register(File)
class Adminfolder(admin.ModelAdmin):
   list_display = ('id','file','filetitle','filedetails')
   
admin.site.register(Details)
class AdminDetails(admin.ModelAdmin):
    list_display = ('id', 'name', 'info') 
 
   

   



