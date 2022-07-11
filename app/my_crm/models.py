from django.db import models

# Create your models here.


class Stages(models.Model):
    title = models.CharField(max_length=20)
    color = models.CharField(max_length=7)

    def __str__(self):
        return self.title
