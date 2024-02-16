from django.shortcuts import render
from .models import Command, Participant
from django.views import View


def index(request):
    teams = Command.objects.order_by('-id')
    teammates = Participant.objects.all()
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'teams': teams, 'teammates': teammates})


def about(request):
    return render(request, 'main/about.html')


def create_team(request):
    return render(request, 'main/create_team.html')


def create_teammate(request):
    return render(request, 'main/create_teammate.html')
