from django.shortcuts import render, redirect
from blog.models import Baloon, BaloonColor, BaloonSize, BaloonType
# Create your views here.
# web шаблонизатор динджа, аджакс

# представление - views.py
# index - главная страница

def index(request):
    # select * from blog_baloons
    baloons = Baloon.objects.all()

    context = {
        'all_baloons':baloons
    }

    return render(request, 'index.html', context)

def index_detail(request, pk):
    # select * from Baloon where id = pk
    baloon = Baloon.objects.get(id=pk)

    context = {
        'baloon': baloon
    }

    return render(request, 'index_detail.html', context)



def ballon_types(request):
    baloons = BaloonType.objects.all()
    context = {
        'ballon_types':baloons
    }
    return render(request, 'ballon_types.html', context)

      
def types_detail(request, pk):
    type_ballon = BaloonType.objects.get(id=pk)

    context = {
        'baloon':type_ballon
    }
    
    return render(request,'type_detail.html', context)
        
  