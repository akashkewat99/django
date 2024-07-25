from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    

class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    rating = models.IntegerField(default=1,validators=[MinValueValidator(5),MinValueValidator(1)])
    author = models.ForeignKey(Author,on_delete=models.CASCADE)

    def __str__(self):
        return self.title