from django.db import models

from django.contrib.auth.models import User
import datetime
import os
# Create your models here.
def get_file_path(request,filename):
    original_filename = filename
    #Khởi tạo nowtime định dạng "năm-tháng-ngày-giờ-phút-giây"
    nowTime = datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
    #filename = YYYYMMDDHH:MM:SS + original_filename
    filename = "%s%s" % (nowTime, original_filename)
    #upload/filename
    return os.path.join("upload/",filename)

# "%" nối chuỗi
class Category(models.Model):
    slug = models.CharField(max_length=100, null=False,blank=False)
    name = models.CharField(max_length=100,null=False,blank=False)
    image = models.ImageField(blank=True,upload_to=get_file_path,null=True)
    description = models.TextField(default=False,)
    status = models.BooleanField(default=False,help_text="0-default,1-Hidden")
    trending = models.BooleanField(default=False,help_text="0-default,1-Trending")
    meta_title = models.CharField(max_length=150,null=False,blank=False)
    meta_keywords = models.TextField(max_length=500,null=False,blank=False)
    create_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
class Product(models.Model):
    category =  models.ForeignKey(Category,on_delete=models.CASCADE)
    slug = models.CharField(max_length=100, null=False,blank=False)
    name = models.CharField(max_length=100,null=False,blank=False)
    product_image = models.ImageField(blank=True,upload_to=get_file_path,null=True)
    small_description = models.CharField(max_length=250,null=False,blank=False)
    quantity = models.IntegerField(default=0,blank=False)
    description = models.TextField(max_length=1000,null=False,blank=False)
    original_price = models.IntegerField(null=False,blank=False)
    selling_price = models.IntegerField(null=False,blank=False)
    status = models.BooleanField(default=False,help_text="0-default,1-Hidden")
    trending = models.BooleanField(default=False,help_text="0-default,1-Trending")
    tag = models.CharField(max_length=100)
    meta_title = models.CharField(max_length=150,null=False,blank=False)
    meta_keywords = models.TextField(max_length=500,null=False,blank=False)
    create_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name