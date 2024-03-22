from .models import Command, Participant
from django.forms import ModelForm


class CommandForm(ModelForm):
    class Meta:
        model = Command
        fields = ['name', 'description']


class ParticipantForm(ModelForm):
    class Meta:
        model = Participant
        fields = ['name', 'command']
