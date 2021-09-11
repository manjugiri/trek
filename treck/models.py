from django.db import models

# Create your models here.
class Packages(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length= 50)
    details = models.CharField(max_length=50)
    altitude = models.CharField(max_length=20)


class Contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    subject = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return self.name

class Safari(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length= 50)

class Treknep(models.Model):
    image = models.ImageField(upload_to='images/')
    





