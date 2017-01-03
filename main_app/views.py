from django.shortcuts import render
from .models import User, Transaction
from django.db.models import Sum
def index(request):
		transactions = Transaction.objects.all()
		return render(request, 'index.html', {'transactions': transactions})
