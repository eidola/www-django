from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from news.models import Article

class IndexView(generic.ListView):
    template_name = 'news/index.html'
    context_object_name = 'article_list'
    
    def get_queryset(self):
        return Article.objects.filter(
            pub_date__lte=timezone.now()
        ).all()


class DetailView(generic.DetailView):
    model = Article
    template_name = 'news/detail.html'

