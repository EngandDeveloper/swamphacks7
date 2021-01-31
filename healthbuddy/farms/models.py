from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

# Create your models here.
class RegisterUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

<<<<<<< HEAD
class Trainer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    city = models.CharField(max_length=60, null=True, blank=True)
    experience = models.IntegerField(max_length=3, null=True, blank=True)
    age = models.IntegerField(max_length=3, null=True, blank=True)
    gender = models.CharField(max_length=60, null=True, blank=True)
    communication = models.CharField(max_length=200, null=True, blank=True)

    objects = models.Manager()

    # def __str__(self):
    #     return self.user

class Babysitter(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    city = models.CharField(max_length=60, null=True, blank=True)
    experience = models.IntegerField(max_length=3, null=True, blank=True)
    age = models.IntegerField(max_length=3, null=True, blank=True)
    gender = models.CharField(max_length=60, null=True, blank=True)
    communication = models.CharField(max_length=200, null=True, blank=True)

    objects = models.Manager()

    # def __str__(self):
    #     return self.user

class GymMember(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    city = models.CharField(max_length=60, null=True, blank=True)
    age = models.IntegerField(max_length=3, null=True, blank=True)
    gender = models.CharField(max_length=60, null=True, blank=True)
    communication = models.CharField(max_length=200, null=True, blank=True)

    objects = models.Manager()

    # def __str__(self):
    #     return self.user
=======
class Trainer():
    print()

class Babysitter():
    print()

class GymMember():
    print()
>>>>>>> main
