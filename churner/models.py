from django.db import models

# Create your models here.

class PredResults(models.Model):
    username = models.CharField(max_length=10)
    Total_trant_Amt = models.IntegerField()
    Edu_level = models.IntegerField()
    Income = models.IntegerField() 
    Total_relationship_cnt = models.IntegerField() 
    Month_on_book = models.IntegerField() 
    Customer_age = models.IntegerField() 
    Contact_cnt_12 = models.IntegerField() 
    Dependent_count = models.IntegerField() 
    gender = models.IntegerField() 
    result = models.IntegerField() 
    
    def __str__(self):
        return self.result
    