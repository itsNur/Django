from django.shortcuts import render
from .models import Command, Participant
from django.views import View
from .forms import CommandForm, ParticipantForm


class IndexView(View):
    def get(self, request):
        teams = Command.objects.all()
        teammates = Participant.objects.all()
        return render(request, 'main/index.html', {'title': 'главная страница сайта', 'teams': teams, 'teammates': teammates})


class AboutView(View):
    def get(self, request):
        return render(request, 'main/about.html')


class CreateTeamView(View):
    def get(self, request):
        team_form = CommandForm()
        context = {'form': team_form}
        return render(request, 'main/create_team.html')


class CreateTeammateView(View):
    def get(self, request):
        teammate_form = ParticipantForm()
        context = {'form': teammate_form}
        return render(request, 'main/create_teammate.html')
