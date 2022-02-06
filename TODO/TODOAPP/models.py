from django.db import models
from datetime import date, datetime

class StudentModel(models.Model):
    created_at = models.DateField(default=date.today)
    name = models.CharField(max_length=255)
    roll = models.CharField(max_length=255)
    section = models.IntegerField()

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Student Model"

    def __str__(self):
        return f"student name : {self.name}"
