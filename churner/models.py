from django.db import models

# Create your models here.

class PredResults(models.Model):
    username = models.CharField(max_length=10)
    Total_Trans_Amt  = models.IntegerField()
    Education_Level  = models.IntegerField()
    Income_Category  = models.IntegerField(null=True) 
    Total_Relationship_Count  = models.IntegerField() 
    Months_on_book  = models.IntegerField() 
    Customer_Age  = models.IntegerField() 
    Contacts_Count_12_mon  = models.IntegerField() 
    Dependent_count  = models.IntegerField() 
    Gender  = models.IntegerField() 
    result = models.IntegerField() 

    