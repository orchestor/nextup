from django.contrib import admin
from music.models import *
# Register your models here.

admin.site.register(song)
admin.site.register(likedSongs)
admin.site.register(purchaseSongs)