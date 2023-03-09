from django.db import models

# Create your models here.


status_choices = (
    ('ToDo', 'ToDo'),
    ('Doing', 'Doing'),
    ('Done', 'Done'),
)


class Task(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(blank=True)
    deadline = models.DateField()
    user = models.CharField(max_length=100)
    status = models.CharField(max_length=100, choices=status_choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} | {self.status} | {self.deadline}'

