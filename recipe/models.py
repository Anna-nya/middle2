from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __iter__(self):
        yield 'name', self.name
