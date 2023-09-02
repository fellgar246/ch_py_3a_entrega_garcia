from django.db import models

# Create your models here.
class user(models.Model):

    name = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    age = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    email = models.EmailField(null=True) 

    def __str__(self):
        return f'{self.name} {self.lastName}'

class Profile(models.Model):
    title = models.CharField(max_length=30)
    aboutMe = models.CharField(max_length=100)
    socialMedia = models.CharField(max_length=100)
    user = models.ForeignKey(user, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} - {self.title}'
    
class entry(models.Model):
    title = models.CharField(max_length=30)
    text =  models.CharField(max_length=300)

    def __str__(self):
        return f'{self.title} - {self.text}'
    
class posts(models.Model):
    title = models.CharField(max_length=30)
    text =  models.CharField(max_length=300)
    user = models.ForeignKey(user, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} - {self.user}'