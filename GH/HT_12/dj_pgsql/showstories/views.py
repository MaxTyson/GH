from django.shortcuts import render
from. models import Showstories, Cat


def showstories(request):
    return render(request, 'showstories/base.html', {'items': Showstories.objects.all()})


