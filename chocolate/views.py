from django.shortcuts import render
from .models import Chocolate

def chocolate_list(request):
    chocolates = Chocolate.objects.all()
    return render(request, 'chocolate/chocolate_list.html', {'chocolates': chocolates})

def chocolate_detail(request, pk):
    chocolate = Chocolate.objects.get(pk=pk)
    return render(request, 'chocolate/chocolate_detail.html', {'chocolate': chocolate})
