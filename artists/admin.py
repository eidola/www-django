from django.contrib import admin
from artists.models import Artist, Link, SocialLink

admin.site.register(Artist)
admin.site.register(Link)
admin.site.register(SocialLink)
