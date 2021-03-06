import markdown

from django.views.generic import DetailView, TemplateView

from news.models import NewsEntry
from .models import FlatPage


class PageDetailView(DetailView):
    """ 
        simple static view. 
        can render markdown or reStructured text
    """

    model = FlatPage
    context_object_name = 'page'
    template_name = 'flatpages/page_detail.html'

    def get_context_data(self, **kwargs):
        context = super(PageDetailView, self).get_context_data(**kwargs)

        if self.object.text_format == 'markdown':
            md = markdown.Markdown(extensions=['markdown.extensions.toc'])
            html = md.convert(context['page'].text)
            toc = md.toc

            context['page'].text = html
            context['page'].toc = toc

        return context


class AboutView(TemplateView):
    template_name = 'flatpages/about.html'

class ServiceProvidersView(TemplateView):
    template_name = 'flatpages/service-providers.html'

class MinutesView(TemplateView):
    template_name = 'flatpages/minutes.html'

    def get_context_data(self, **kwargs):
        context = super(TemplateView, self).get_context_data(**kwargs)
        context['minutes_entry_list'] = NewsEntry.objects\
            .filter(title__icontains='minutes')\
            .order_by('-pub_date')
        return context
