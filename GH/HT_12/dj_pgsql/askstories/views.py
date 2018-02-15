from django.shortcuts import render
from. models import Askstories
from showstories.models import Cat


def askstories(request):
    return render(request, 'askstories/base.html', {'items':
                                                    Askstories.objects.all()})

def categories(request):
    return render(request, 'askstories/wrap.html', {'categories':
                                                    Cat.objects.all()})
