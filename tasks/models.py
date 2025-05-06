from django.db import models

class Task(models.Model):
    PRIORITY_CHOICES=[
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]

    title=models.CharField(max_length=200)
    completed=models.BooleanField(default=False)
    priority=models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='Medium')
    due_date=models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title
