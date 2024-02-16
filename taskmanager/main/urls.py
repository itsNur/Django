from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('about-us', views.about, name='about'),
    path('create_team', views.create_team, name='create_team'),
    path('create_teammate', views.create_teammate, name='create_teammate')
]
