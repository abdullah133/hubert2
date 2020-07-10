from django.shortcuts import render
# Create your views here.
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from .forms import KontaktForm
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import send_mail
from .models import  KontaktInfo

class ContactView(FormView):
    template_name = 'contact_app/contact.html'
    form_class = KontaktForm
    success_url = reverse_lazy('contact_app:contact_erfolg_page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        kontakt_angaben = KontaktInfo.objects.all()
        context['kontakt_angaben'] = kontakt_angaben

        return context

    def form_valid(self, form):

        user_email = form.cleaned_data['user_email']
        betreff = form.cleaned_data['betreff']
        name = form.cleaned_data['name']
        nachricht = form.cleaned_data['nachricht']
        subject = 'Ihr habt eine neue Nachricht!'
        message = 'Ihr habt eine neue Nachricht'
        msg_html = render_to_string('contact_app/emails/email_contact.html', {'user_email':user_email,
                                                                                'name':name,
                                                                                'betreff':betreff,
                                                                                'nachricht':nachricht,})

        eigene_mail_adresse = settings.DEFAULT_FROM_EMAIL
        to_list = [eigene_mail_adresse,]

        send_mail(subject=subject,message=message, from_email=eigene_mail_adresse, recipient_list=to_list,html_message=msg_html,)



        return super().form_valid(form)

class ContactViewErfolg(TemplateView):
    template_name = 'contact_app/contact_erfolg.html'
