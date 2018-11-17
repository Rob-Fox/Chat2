from __future__ import unicode_literals
from django.db import models
import re
import bcrypt

# Create your models here.

class User_Manager(models.Manager):
    def reg_validator(self, postData):
        errors = {}
        if len(postData['Username']) < 3:
            errors['Username'] = "Username must be at least 3 characters"
        if len(postData['Username']) > 255:
            errors['Username'] = "Username must not be more than 255 characters"
        if User.objects.filter(Username = postData['Username']):
            errors['Username'] = "Username is already in use, please try a different Username"
        if postData['Password'] != postData['C_Password']:
            errors['Password'] = "Please enter matching Passwords in both boxes"
        if len(postData['Password']) < 6:
            errors['Password'] = "Please create a Password that is at least 6 characters"
        if len(postData['Password']) > 20:
            errors['Password'] = "Please select a Password that is 20 or fewer characters"
        return errors

    def login_validator(self, postData):
        errors={}
        if not User.objects.filter(Username = postData['L_Username']):
            errors['L_Username'] = "There is no account matching that Username"
        if len(postData['L_Password']) < 6:
            errors['L_Password'] = "Please enter a valid Password"
        # if User.objects.filter(Username = postData['L_Username']):
        #     if not bcrypt.checkpw(postData['L_Password'].encode(), User.objects.get(Username = postData['L_Username']).Password.encode()):
        #         errors['L_Password'] = "It seems that is not a matching Username and Password. Please try again"
        return errors

class User(models.Model):
    Username = models.CharField(max_length=255)
    Password = models.CharField(max_length=255)
    Created_At = models.DateTimeField(auto_now_add = True)
    objects = User_Manager()
    # Room_List = 
    # Invites_List = 

    def __repr__(self):
        return 'Username: {}, Password: {}, Created: {}'.format(self.Username, self.Password, self.Created_At)
