from django.shortcuts import render, redirect
from .forms import ContactForm

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
