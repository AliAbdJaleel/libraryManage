from datetime import timezone
from django.db import models
from django.utils import timezone
# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=100)
    piography = models.TextField(max_length=20000)

    def __str__(self):
        return self.name
    

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey('Author',related_name='book_author',on_delete=models.CASCADE)
    publication_date = models.DateTimeField(default=timezone.now)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title

class Review(models.Model):
    book = models.ForeignKey('Book',related_name='review_book',on_delete= models.SET_NULL,null=True)
    reviewer_name = models.CharField(max_length=100)
    content = models.TextField(max_length=20000)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.reviewer_name