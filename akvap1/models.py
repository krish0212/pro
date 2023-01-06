from django.db import models
   
# Create your models here.
class Member(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    address = models.CharField (max_length=50, null=True)
    #file = models.FileField()
    
    
    class Meta:  
        db_table = "tbl_member"
        #fields = "null"