from pyexpat import model
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField
from django.forms import IntegerField
# Create your models here.

class userAll(AbstractUser):
    role = models.CharField(max_length=50,null=True)
    image = models.TextField(null=True)

class Projects(models.Model):
    proj_id = models.IntegerField(primary_key=True)
    proj_name = models.CharField(max_length=50,null=True)
    proj_discription = models.TextField(null=True)
    proj_frontend_language = models.CharField(max_length=100,null=True)
    proj_backend_language = models.CharField(max_length=100,null=True)
    proj_status = models.CharField(max_length=50,null=True)
    proj_manager_id = models.ForeignKey(userAll,on_delete=models.CASCADE)
    
class Tech_stack(models.Model):
    tech_id = models.IntegerField(primary_key=True)
    tech_label = models.CharField(max_length=50,null=True)

class Dev_stack(models.Model):
    dev_id = models.IntegerField(primary_key = True)
    proj_id = models.ForeignKey(Projects,on_delete=models.CASCADE)
    tech_id = models.ForeignKey(Tech_stack,on_delete=models.CASCADE)
    dev_id = models.ForeignKey(userAll,on_delete=models.CASCADE)


class Tags(models.Model):
    tag_id = models.IntegerField(primary_key=True)
    tag_name = models.CharField(max_length=50,null=True)


class Solution(models.Model):
    solution_id = models.IntegerField(primary_key=True)
    solution = models.TextField(null=True)
    user_id = models.ForeignKey(userAll,on_delete=models.CASCADE)

class voting(models.Model):
    vot_id = models.IntegerField(primary_key=True)
    upvote = models.BooleanField()
    downvote = models.BooleanField()
    solution_id = models.ForeignKey(Solution,on_delete=models.CASCADE)
    user_id = models.ForeignKey(userAll,on_delete=models.CASCADE)



class Error(models.Model):
    err_Id = models.IntegerField(primary_key=True)
    err_status = models.CharField(max_length=50,null=True)
    err_occured = models.DateTimeField(auto_now_add=True)
    err_module = models.CharField(max_length=50, null=True)
    err_priority = models.CharField(max_length=50,null=True)
    err_image = models.TextField(null=True)
    proj_id = models.ForeignKey(Projects,on_delete=models.CASCADE)
    dev_stack_id = models.ForeignKey(Dev_stack,on_delete=models.CASCADE)
    resolver_id = models.ForeignKey(userAll,on_delete=models.CASCADE)
    solution_id = models.ManyToManyField(Solution,null=True)
    tag_id = models.ManyToManyField(Tags)








