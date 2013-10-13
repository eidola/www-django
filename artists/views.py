from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from artists.models import Artist

class IndexView(generic.ListView):
    template_name = 'artists/index.html'
    context_object_name = 'artists_list'
    
    def get_queryset(self):
        return Artist.objects.filter(
            pub_date__lte=timezone.now()
        ).all()


class DetailView(generic.DetailView):
    model = Artist
    template_name = 'artists/detail.html'
