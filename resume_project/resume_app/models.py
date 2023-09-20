from django.db import models

class Experience(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()

class Education(models.Model):
    degree = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()

class Resume(models.Model):
    name = models.CharField(max_length=100)
    contact_details = models.CharField(max_length=200)
    summary = models.TextField()
    experiences = models.ManyToManyField(Experience)
    educations = models.ManyToManyField(Education)
