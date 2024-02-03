from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView

from .models import Contact
from .forms import ContactForm
from django.contrib.auth.forms import UserCreationForm


class HomePageView(TemplateView):
    template_name = 'base.html'



def update_contact(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)

    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            # Redirect or show success message
    else:
        form = ContactForm(instance=contact)

    return render(request, 'update_contact.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to login or home
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})
