from django.urls import path
from ProfileApp import views

urlpatterns = [

    path('', views.home, name='home'),
    path('test', views.tests, name='test'),
    path('profile', views.profile, name='profile'),
    path('education', views.education, name='education'),
    path('interests', views.interests, name='interests'),
    path('dreamJob', views.dreamJob, name='dreamJob'),
    path('idol', views.idol, name='idol'),
    path('hny', views.hny, name='hny'),
]
