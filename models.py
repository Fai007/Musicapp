from django.db import models

# Create your models here.
class Artiste(models.Model):
    first_name = models.CharField(max_length=500)
    last_name = models.CharField(max_length=500)
    age= models.IntegerField()

class Lyrics(models.Model):
    song_id= models.IntegerField()
    content= models.CharField(max_length=1000000)

class Song(models.Model):
    Artiste= models.ForeignKey(Artiste, on_delete=models.PROTECT)
    title= models.CharField(max_length=500)
    date_releases= models.DateField()
    likes= models.IntegerField()
    artiste_id= models.IntegerField()
