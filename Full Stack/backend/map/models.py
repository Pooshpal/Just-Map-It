from django.db import models

# Create your models here.

class List(models.Model):
    name = models.CharField(max_length=120)
    quantity = models.IntegerField()
    purchased = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name