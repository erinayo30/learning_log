from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model =Topic
        fields =['text']
        labels = {'text': 'What topic are you learning'}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields =['text']
        labels = {'text': 'Short Note'}
        widgets = {'text': forms.Textarea(attrs={'cols':80})}

# adding the CustomUserCreationFrom
class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30,
                                 required=True,
                                 widget=forms.TextInput(attrs={
                                     'class':'form-control',
                                     'placeholder':'First Name'})
                                 )
    last_name = forms.CharField(max_length=30,
                                 required=True,
                                 widget=forms.TextInput(attrs={
                                     'class': 'form-control',
                                     'placeholder': 'Last Name'})
                                 )
    other_name = forms.CharField(max_length=30,
                                 required=False,
                                 widget=forms.TextInput(attrs={
                                     'class': 'form-control',
                                     'placeholder': 'Other Name'})
                                 )
    phone_number = forms.CharField(max_length=15,
                                 required=True,
                                 widget=forms.TextInput(attrs={
                                     'class': 'form-control',
                                     'placeholder': 'Enter your phone number'})
                                 )
    email = forms.EmailField(max_length=254,
                             required=True,
                             widget=forms.EmailInput(attrs={
                                 'class': 'form-control',
                                'placeholder': 'Enter your email address'
                             })
                             )
class Meta:
    model = User
    fields = ['username', 'first_name', 'last_name', 'email']
def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    # Add custom styling to existing UserCreationForm fields
    self.fields['username'].widget.attrs.update({
        'class': 'form-control',
        'placeholder':'Enter your username'
    })
    self.fields['password'].widget.attrs.update({
        'class': 'form-control',
        'placeholder':'Enter Password'
    })
    self.fields['password2'].widget.attrs.update({
        'class': 'form-control',
        'placeholder':'Confirm Password'
    })
def clean_email(self):
    email = self.cleaned_data.get('email')
    if User.objects.filter(email=email).exists():
        raise ValidationError("Email already exists")
    return email
def clean_phone_number(self):
    phone_number = self.cleaned_data.get('phone_number')
    phone_number_clean =''.join(filter(str.isdigit, phone_number))

    if not phone_number_clean:
        raise ValidationError("Phone number cannot be empty")

    if len(phone_number_clean) > 11:
        raise ValidationError("Phone number cannot be more than 11 digits")

    if len(phone_number_clean) >11:
        raise ValidationError("Phone number cannot be more than 11 digits")
    return phone_number_clean

def save(self, commit=True):
    user= super().save(commit=False)
    user.first_name = self.cleaned_data['first_name']
    user.last_name = self.cleaned_data['last_name']
    user.email = self.cleaned_data['email']

    if commit:
        user.save()

        return user