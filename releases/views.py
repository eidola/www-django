from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from releases.models import Release

class IndexView(generic.ListView):
    template_name = 'releases/index.html'
    context_object_name = 'releases_list'
    
    def get_queryset(self):
        return Release.objects.filter(
            pub_date__lte=timezone.now()
        ).all()


class DetailView(generic.DetailView):
    model = Release
    template_name = 'releases/detail.html'
