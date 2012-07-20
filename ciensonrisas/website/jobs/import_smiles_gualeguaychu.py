# -*- coding: utf-8 -*-

import glob

from django.core.files.base import ContentFile

from django_extensions.management.jobs import BaseJob

from website.models import Author
from website.models import Smile
from website.models import Place


class Job(BaseJob):
    help = 'Import Smiles\' pictures already taken'

    def execute(self):
        files = glob.glob('/home/humitos/ciensonrisas/sonrisas/gualeguaychu/*')
        files = sorted(files, key=lambda x: int(x.replace('\xcc\x81', '').split('#')[1].split(' ')[0]))
        for f in files:
            number = int(f.replace('\xcc\x81', '').split('#')[1].split(' ')[0])
            smile = Smile(number=number,
                          place=Place.objects.filter(name=u'Gualeguaychú')[0],
                          author=Author.objects.get(id=1))
            smile.photo = f
            smile.photo.save(f, ContentFile(open(f).read()))
            smile.save()
