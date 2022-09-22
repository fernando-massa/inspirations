from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date


# Create your models here please

class Gallery(models.Model):  # IS A
    name = models.CharField(max_length=100)  # HAS A
    description = models.TextField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # inspirations = models.ManyToManyField(Inspiration)

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse('galleries_detail', kwargs={'pk': self.id})




class Inspiration(models.Model):
    name = models.CharField(max_length=500)
    description = models.CharField(max_length=1000)
    link = models.CharField(max_length=1000)

    # #photo testing
    # photo_file = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=100)

    galleries = models.ManyToManyField(Gallery)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('inspirations_detail', kwargs={'pk': self.id})
    

class Photo(models.Model):
    url = models.CharField(max_length=400)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    inspiration = models.ForeignKey(Inspiration, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for inspiration_id: {self.inspiration_id} @{self.url}"


class Note(models.Model):
    date = models.DateField()
    note = models.TextField(max_length=1000)

    inspiration = models.ForeignKey(Inspiration, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.note} {self.date}"

    class Meta:
        ordering = ['-date']