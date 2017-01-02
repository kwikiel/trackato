from django.shortcuts import render
from .models import Treasure
from django.db.models import Sum
def index(request):
		treasures = Treasure.objects.all()
		total = Treasure.objects.aggregate(Sum('value'))
		return render(request, 'index.html', {'treasures': treasures, 'total': total})
