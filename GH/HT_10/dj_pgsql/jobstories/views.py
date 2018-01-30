from django.shortcuts import render
from. models import Jobstories


def jobstories(request):
    return render(request, 'jobstories/base.html', {'items':
                                                    Jobstories.objects.all()})
