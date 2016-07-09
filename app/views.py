from django import forms
from django.http import HttpResponse
from django.shortcuts import redirect
from django.core.mail import send_mail
from django.views.generic import TemplateView
from django.contrib import messages

from captcha.fields import ReCaptchaField

# from membernews.models import MemberNewsEntry
from news.models import NewsEntry

class ContactForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=200)
    email = forms.CharField(label='Your email', max_length=200)
    message = forms.CharField(widget=forms.Textarea)
    captcha = ReCaptchaField()


class HomeView(TemplateView):
    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs):
        context = super(TemplateView, self).get_context_data(**kwargs)
        context['news_entry_list'] = NewsEntry.objects.filter(newstype='news').order_by('-pub_date')
        context['news_entry_list_small'] = NewsEntry.objects.order_by('-pub_date')
        context['membernews_entry_list'] = NewsEntry.objects.filter(newstype='membernews').order_by('-pub_date')
        context['contact_form'] = ContactForm
        return context

def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            sender = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            body = 'message from: {sender}, {email} \n\n {message}'.format(**locals())
            send_mail(
                'SSIP209 "Contact Us" Message from {}'.format(sender),
                body,
                'noreply@ssip209.org',
                ['max.atreides@gmail.com'],
                fail_silently=False,
            )
            messages.success(request, "Thank you! Your message has been sent to us.")
    return redirect('home')
