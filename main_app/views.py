from django.shortcuts import render
from .models import Treasure

def index(request):
    treasures = Treasure.objects.all()
    return render(request, 'index.html', {'treasures': treasures})

def detail(request, treasure_id):
    treasure = Treasure.objects.get(id=treasure_id)
    return render(request, 'detail.html', {'treasure': treasure})
