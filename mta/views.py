from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'mta/index.html', {'title': 'Home'})

def leaderboard(request):
    return render(request, 'mta/leaderboard.html', {'title': 'Leaderboard'})

def market(request):
    return render(request, 'mta/market.html', {'title': 'Market'})

def portfolio(request):
    return render(request, 'mta/portfolio.html', {'title': 'Portfolio'})

def profile(request):
    return render(request, 'mta/profile.html', {'title': 'Profile'})