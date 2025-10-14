from django.db import models

# Create your models here.
class mystudents(models.Model):
    name = models.CharField(max_length=20)
    course = models.CharField(max_length=20)
    stdno = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name}, {self.course}, {self.stdno}"