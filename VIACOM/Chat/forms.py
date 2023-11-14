from django import forms
from .models import Contact, CONTACT_TYPE

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        # fields = ['name', 'email', 'type', 'message'] or
        fields = '__all__'



class ContactForm2(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(help_text= 'enter a valid email')
    type = forms.ChoiceField(choices=CONTACT_TYPE)
    message = forms.CharField (widget=forms.Textarea)