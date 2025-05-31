from django.db import models

class Task(models.Model):
    STATUS_CHOICES=[
        ('Not Started','Not Started'),
        ('Started','Started'),
    ]

    title=models.CharField(max_length=200)
    status=models.CharField(max_length=20,choices=STATUS_CHOICES,default='Not Started')
    priority=models.CharField(max_length=10,choices=[('Low','Low'),('Medium','Medium'), ('High','High')],default='Low')
    due_date=models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title
