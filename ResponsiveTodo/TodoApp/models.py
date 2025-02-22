from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    category = models.CharField(max_length=10)
    uploaded = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()


    def __str__(self):
        return self.title