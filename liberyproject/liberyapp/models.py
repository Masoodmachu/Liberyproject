from django.db import models


class Book(models.Model):
    title=models.CharField(max_length=20)
    author=models.CharField(max_length=25)
    price=models.IntegerField()
    cover=models.ImageField(upload_to='book/image',null=True,blank=True)
    pdf=models.FileField(upload_to='book/pdf')

    def __str__(self):
        return self.title

