# -*- coding: utf-8 -*-
import os

from django.core.files.base import ContentFile
from django_extensions.management.jobs import BaseJob

from website.models import Author
from website.models import Place

from django.conf import settings

MOCKUPS_PATH = os.path.join(settings.PROJECT_ROOT, '..', '..', 'mockups')

PLACES = [(u'Concepción del Uruguay', u'Entre Ríos, Argentina',
           os.path.join(MOCKUPS_PATH, 'place_example_thumb_cdu.jpg')),
          (u'Santa Fe', 'Santa Fe, Argentina',
           os.path.join(MOCKUPS_PATH, 'place_example_thumb_stafe.jpg')),
          (u'Gualeguaychú', u'Entre Ríos, Argentina',
           os.path.join(MOCKUPS_PATH, 'place_example_thumb_gchu.jpg'))]


class Job(BaseJob):
    help = 'Create default Places and Author'

    def execute(self):
        for name, description, photo in PLACES:
            place = Place(name=name, description=description)
            place.photo = photo
            place.photo.save(photo, ContentFile(open(photo).read()))
            place.save()

        author = Author(
            first_name=u'Nicolás',
            last_name=u'Pereyra',
            nickname=u'Soy el Nes',
            description=u'Nothing to say')
        photo = os.path.join(MOCKUPS_PATH, 'place_example_thumb_cdu.jpg')
        author.photo = photo
        author.photo.save(photo, ContentFile(open(photo).read()))
        author.sign = photo
        author.sign.save(photo, ContentFile(open(photo).read()))
        author.save()
