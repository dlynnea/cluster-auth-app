from django.db import models

class Headline(models.Model):
    title = models.CharField(max_length=120)
    url = models.TextField()

    def __str__(self):
        return self.title

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='books/pdfs/')

    def __str__(self):
        return self.title
