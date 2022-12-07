from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    rollno = models.PositiveIntegerField()

    def __str__(self):
        return self.name

