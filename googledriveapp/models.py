from django.db import models
from django.contrib.auth.models import User
import os
# Create your models here.
class Folder(models.Model):
    foldername = models.CharField(max_length=50)
    folderdesc = models.CharField(max_length=255)
    folderuser = models.ForeignKey(User,on_delete=models.CASCADE)
class File(models.Model):
    filetitle = models.CharField(max_length=50)
    folder = models.ForeignKey(Folder,on_delete=models.CASCADE)
    file = models.FileField(upload_to="Files")
    filedetails = models.name = models.CharField(max_length=50, blank=False)
    
    def save(self, *args, **kwargs):
        
        file_extension = os.path.splitext(self.file.name)[1].lower()
        file_type = None

        
        if file_extension in ['.jpg', '.jpeg', '.png', '.gif']:
            file_type = 'Image'
        elif file_extension in ['.pdf']:
            file_type = 'PDF'
        elif file_extension in ['.doc', '.docx']:
            file_type = 'Word'
        elif file_extension in ['.xls', '.xlsx']:
            file_type = 'Excel'
        else:
            self.filedetails = "Unknown"
            
        self.filedetails = file_type
        super(File, self).save(*args, **kwargs)   
            
class Details(models.Model):
    name = models.CharField(max_length=50)
    info = models.CharField(max_length=255)