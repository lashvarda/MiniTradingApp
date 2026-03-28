import django.conf.urls
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='/'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('market/', views.market, name='market'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
]