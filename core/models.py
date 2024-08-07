from django.db import models

# Create your models here.
class Todo(models.Model):
    
    date_created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    task_details = models.TextField(max_length=1000)
    status = models.CharField(max_length=20, choices=(
        ('in_progress', 'In Progress'),
        ('complete', 'Complete'),
        
    ))
    due_date = models.DateTimeField()   
    
    def __str__(self):
        return f'Title: {self.title} '