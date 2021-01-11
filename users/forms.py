from django import forms


class ContactForm(forms.Form):
    username = forms.CharField(max_length=50, required=False)
    email = forms.EmailField(max_length=254, required=True)
    subject = forms.CharField(max_length=20, required=True)
    message = forms.CharField(
        max_length=3000,
        widget=forms.Textarea(),
        help_text='Write your message here!', 
        required=True)