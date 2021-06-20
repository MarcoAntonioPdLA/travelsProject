from django.shortcuts import render
from .models import Destination

# Create your views here.
def index(request):
  context = {}
  destinations = Destination.objects.all()
  context['destinations'] = destinations
  return render(request, 'index.html', context)
