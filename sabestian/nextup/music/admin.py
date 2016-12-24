from django.contrib import admin
from music.models import song, likedSongs
# Register your models here.

admin.site.register(song)
admin.site.register(likedSongs)