from django.views.generic import TemplateView

# from membernews.models import MemberNewsEntry
from news.models import NewsEntry

class HomeView(TemplateView):
    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs):
        context = super(TemplateView, self).get_context_data(**kwargs)
        context['news_entry_list'] = NewsEntry.objects.filter(newstype='news')
        context['membernews_entry_list'] = NewsEntry.objects.filter(newstype='membernews')
        return context
