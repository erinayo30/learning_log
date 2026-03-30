from django import forms

from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model =Topic
        fields ={'text'}
        labels = {'text': 'What topic are you learning'}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields ={'text'}
        labels = {'text': 'Short Note'}
        widgets = {'text': forms.Textarea(attrs={'cols':80})}