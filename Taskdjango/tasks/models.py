from django.db import models

# Create your models here.
class Task(models.Model):
    
    task_number = models.IntegerField()

    
    task_name = models.CharField(max_length=200)

    
    task_description = models.TextField()

    
    task_deadline_date = models.DateField()

    
    STATUS_CHOICES = [
        ('completed', 'Completed'),
        ('pending', 'Pending'),
    ]
    task_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f'tasks: {self.task_name} - {self.task_status}' 