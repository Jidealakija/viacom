from django.shortcuts import render, redirect
from .forms import ContactForm, ContactForm2


def home(request):
    return render(request, 'Chat/home.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return redirect('contact')
        
    else:
        form = ContactForm()
    context = {'form': form}
    return render(request, 'Chat/contact.html', context)

#DjangoForms

from .models import Contact
from django.contrib import messages

def contact2 (request):
    if request.method == 'POST':
        form = ContactForm2(request.POST)
        if form.is_valid():
            input_name = form.cleaned_data.get('name')
            input_email = form.cleaned_data.get('email')
            input_type = form.cleaned_data.get('type')
            input_message = form.cleaned_data.get('message')

            Contact.objects.create(name=input_name, email = input_email,
                                   type = input_type, message = input_message)
            messages.success(request, 'Thank you for contacting us')
            return redirect('/')
        else:
            messages.error(request, 'oops, something went wrong')
            return redirect('contact2')
    else:
        form = ContactForm2()
    context = {'form': form}
    return render(request, 'chat/contact2.html', context)


#htmlforms

def contact3 (request):
    if request.method == 'POST':
        input_name = request.POST.get('name')
        input_email = request.POST.get('email')
        input_type = request.POST.get('type')
        input_message = request.POST.get('message')

        if len(input_name) > 100:
            messages.error(request, 'name is too long')
            return redirect('contact3')
        elif input_type == '':
            messages.error(request, 'type cannot be empty')
            return redirect ('contact3')
        elif input_email == '':
            messages.error(request, 'email cannot be empty')
            return redirect ('contact3')
        elif input_message == '':
            messages.error(request, 'messages cannot be empty')
            return redirect ('contact3')
        else:
            Contact.objects.create(name=input_name, email = input_email,
                                   type = input_type, message = input_message)
            messages.success(request, 'Thanks for contacting us')
            return redirect('/')
        
    else:
        return render(request, 'Chat/contact3.html')
