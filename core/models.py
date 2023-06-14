from django.db import models

class PresenceModel(models.Model):
    student_name = models.CharField(max_length=100)
    professor_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title