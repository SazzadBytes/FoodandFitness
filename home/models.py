from django.db import models

# Create your models here.
class SignUp(models.Model):
    fname=models.CharField(max_length=100)
    uname=models.CharField(max_length=100)
    dob=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    umail=models.CharField(max_length=100)
    pnumber=models.CharField(max_length=100)
    pass1=models.CharField(max_length=100)
    pass2=models.CharField(max_length=100)

class FoodTips(models.Model):
    foodname=models.CharField(max_length=100)
    foodnutrations=models.TextField()
    fooddescriptions=models.TextField()
    fooddanger=models.TextField()
    whocaneat=models.TextField()
    
class Bmi(models.Model):
    bmitype=models.CharField(max_length=100)
    bmidescription=models.TextField()

class BloodPresure(models.Model):
    presuretype=models.CharField(max_length=100)
    presuredescription=models.TextField()

class Sugar(models.Model):
    sugartype=models.CharField(max_length=100)
    sugardescription=models.TextField()


class Update(models.Model):
    bmi=models.CharField(max_length=100,default="0")
    bp=models.CharField(max_length=100,default="0")
    bs=models.CharField(max_length=100,default="0")
    unamep=models.CharField(max_length=100, null=True)
    
    
class FoodBlog(models.Model):
    title=models.CharField(max_length=250)
    description=models.TextField()
    writter=models.CharField(max_length=100)
    slug = models.SlugField(unique=True,null=True)

class HealthBlog(models.Model):
    title=models.CharField(max_length=250)
    description=models.TextField() 
    writter=models.CharField(max_length=100)
    slug = models.SlugField(unique=True,null=True)
