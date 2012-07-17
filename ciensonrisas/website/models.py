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
    place = models.ForeignKey('Place')
    author = models.ForeignKey('Author')

    def __unicode__(self):
        return '# %s' % self.number


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    nickname = models.CharField(max_length=30)
    description = models.TextField()
    photo = models.ImageField(upload_to='authors')
    sign = models.ImageField(upload_to='signs')

    def __unicode__(self):
        return self.nickname
