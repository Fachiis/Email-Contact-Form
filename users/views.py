from django.http.response import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from users.forms import ContactForm
from django.shortcuts import redirect, render
from django.core.mail import send_mail, BadHeaderError

from .forms import ContactForm

def home(request):
    if request.method == 'GET':
       form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, email, ['admin@site.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
        else:
            return HttpResponse('Sorry, message not sent')
    return render(request, 'home.html', {'form':form})


class SuccessView(TemplateView):
    template_name = 'success.html'
