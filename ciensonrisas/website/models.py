from django.db import models


class Place(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    photo = models.ImageField(upload_to='places')

    def __unicode__(self):
        return self.name


class Smile(models.Model):
    number = models.IntegerField()
    description = models.TextField()
    photo = models.ImageField(upload_to='smiles')
    place = models.ForeignKey(Place)
