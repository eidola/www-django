from django.contrib import admin
from releases.models import Release, Track, ReleaseLicense

admin.site.register(Release)
admin.site.register(Track)
admin.site.register(ReleaseLicense)
