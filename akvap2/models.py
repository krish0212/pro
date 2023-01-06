from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    city = models.CharField (max_length=50, null=True)
    #phone = models.CharField(max_length=50, null=True)
    
    class Meta:  
        db_table = "t_users"
        #fields = "null"