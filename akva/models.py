from django.db import models
  
# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    city = models.CharField (max_length=50, null=True)
   
    def __str__(self):
            return self.name
    
    class Meta:  
        db_table = "t_users"
       