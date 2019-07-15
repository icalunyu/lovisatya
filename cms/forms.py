from django import forms
from cms.models import Rsvp

class InvitationForms(forms.ModelForm):
    class Meta:
        model = Rsvp
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Full Name'}),
            'email': forms.TextInput(attrs={'placeholder': 'Your Email'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Your Phone Number'}),
            'keypass': forms.TextInput(attrs={'placeholder': 'Code'}),
            'message': forms.Textarea(attrs={'placeholder': 'Share your thought for Bride and Groom'}),
        }
