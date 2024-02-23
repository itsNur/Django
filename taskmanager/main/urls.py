from django.urls import path
from .views import IndexView, AboutView, CreateTeamView, CreateTeammateView


urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('about-us', AboutView.as_view(), name='about'),
    path('create_team', CreateTeamView.as_view(), name='create_team'),
    path('create_teammate', CreateTeammateView.as_view(), name='create_teammate')
]
