from django.shortcuts import render
from. models import Askstories


def askstories(request):
    return render(request, 'askstories/base.html', {'items':
                                                    Askstories.objects.all()})
