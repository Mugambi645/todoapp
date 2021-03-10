from django.db import models

# Create your models here.
class Work(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(default="content")
    started = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
#string representation of name
    def __str__(self):
        return self.name