from django.db import models
from django.utils import timezone

class Books(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=300)
    publication_date = models.DateTimeField(default=timezone.now)
    publisher = models.CharField(max_length=200)
    summary = models.TextField()
    price = models.DecimalField(max_digits= 6, decimal_places=2)
    linkToBuy = models.URLField(max_length=400)
    image = models.URLField(max_length=400)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title