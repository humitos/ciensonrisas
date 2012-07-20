from django.views.generic import DetailView
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

from website.models import Place
from website.models import Smile
from website.models import Message


class PlaceDetailView(DetailView):

    queryset = Place.objects.all()

    def get_object(self):
        # Call the superclass
        object = super(PlaceDetailView, self).get_object()
        # Record the last accessed date
        # object.last_accessed = datetime.datetime.now()
        # object.save()
        # Return the object
        return object


class SmileDetailView(DetailView):

    queryset = Smile.objects.all()

    def get_object(self):
        # Call the superclass
        object = super(SmileDetailView, self).get_object()
        # Record the last accessed date
        # object.last_accessed = datetime.datetime.now()
        # object.save()
        # Return the object
        return object


class IndexTemplateView(TemplateView):
    pass


class MessageCreate(CreateView):
    model = Message
