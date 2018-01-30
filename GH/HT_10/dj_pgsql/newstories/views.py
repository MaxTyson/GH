from django.shortcuts import render
from. models import Newstories
# Create your views here.

def newstories(request):
    return render(request, 'newstories/base.html', {'items':
                                                    Newstories.objects.all()})
