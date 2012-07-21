from django.contrib import admin

from website.models import Place
from website.models import Smile
from website.models import Author
from website.models import Message


class PlaceAdmin(admin.ModelAdmin):
    pass


class SmileAdmin(admin.ModelAdmin):
    pass


class AuthorAdmin(admin.ModelAdmin):
    pass


class MessageAdmin(admin.ModelAdmin):
    pass

admin.site.register(Place, PlaceAdmin)
admin.site.register(Smile, SmileAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Message, MessageAdmin)
