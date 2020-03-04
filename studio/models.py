from django.db import models

class Achievement(models.Model):
    caption = models.CharField(max_length=80)
    count = models.IntegerField()
    img_url = models.CharField(max_length=2048)

class Testimonial(models.Model):
    name = models.CharField(max_length=80)
    testi = models.TextField(max_length=9999)

class FormSubmission(models.Model):
    name = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.EmailField()
    message = models.CharField(max_length=10000)