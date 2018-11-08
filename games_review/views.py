from django.shortcuts import render
from games_review.models import Game, Type

# Create your views here.

def index(request):
    games = Game.objects.all()
    return render(request, 'index.html', {'latests_games': games})

def game(request, slug):
    game = get_object_or_404(Game, slug=slug)
    return render(request, 'game.html', {'game': game})