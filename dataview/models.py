from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class UserData(models.Model):
    
    compname = models.CharField(max_length=250)                 # ZAHARENKOVAAA
    disk = models.CharField(max_length=2)                       # E
    folder = models.CharField(max_length=250)                   # inst\CorelDRAW.Graphics.Suite X7.17.4.0.887.Special.Edition.RePack.by.ALEX\OpenSource\CorelPS2PDF\
    is_profile = models.BooleanField()                          # True if c:\Users etc...
    filename_long = models.CharField(max_length=250)            # CorelPS2PDF.vcxproj.filters
    filename_shot = models.CharField(max_length=250)            # CorelPS2PDF
    ext_long = models.CharField(max_length=250)                 # vcxproj.filters
    ext_shot = models.CharField(max_length=250)                 # filters
    size = models.BigIntegerField()                             # 1323    
    fullname = models.TextField()                               # E:\inst\CorelDRAW.Graphics.Suite X7.17.4.0.887.Special.Edition.RePack.by.ALEX\OpenSource\CorelPS2PDF\CorelPS2PDF.vcxproj.filters
    year = models.IntegerField()                                # 2019
    month = models.IntegerField()                               # 8
    creationtime = models.DateTimeField(auto_now_add=True)      # 27.08.2019 16:46:53
    fio = models.CharField(max_length=250)                      # Захаренкова Илона Давыдовна
    otdel = models.CharField(max_length=250)                    # Издательский
    textfull = models.TextField()                               # inst CorelDRAW Graphics Suite X7 17 4 0 887 Special Edition RePack by ALEX OpenSource CorelPS2PDF CorelPS2PDF vcxproj filters
    textless = models.TextField()                               # 
    lastupdate = models.DateTimeField(auto_now_add=True)

    #slug = models.SlugField(max_length=250, unique_for_date='publish')
    #publish = models.DateTimeField(default=timezone.now)
    #author = models.ForeignKey(User, related_name='blog_posts')
    
    
    
class Meta:
    indexes = [
   models.Index(fields=['compname', 'folder','fullname',]),
]

def __str__(self):
    return self.title