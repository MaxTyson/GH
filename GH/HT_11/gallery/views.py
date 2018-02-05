from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Like, Photo


class IndexView(generic.ListView):
    template_name = 'gallery/index.html'
    context_object_name = 'latest_photos_list'

    def get_queryset(self):
        return Photo.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Photo
    template_name = 'gallery/detail.html'


class ResultsView(generic.DetailView):
    model = Photo
    template_name = 'gallery/results.html'


def add_like(request, photo_id):
    name = get_object_or_404(Photo, pk=photo_id)
    try:
        selected_like = name.like_set.get(pk=request.POST['like'])
    except (KeyError, Like.DoesNotExist):
        # Redisplay the question add like form.
        return render(request, 'gallery/detail.html', {
            'name': name,
            'error_message': "You didn't add a like.",
        })
    else:
        selected_like.likes += 1
        selected_like.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('gallery:results', args=(photo.id,)))


# def index(request):

#     latest_photos_list = Photo.objects.order_by('-pub_date')[:5]
#     context = {'latest_photos_list': latest_photos_list}
#     return render(request, 'gallery/index.html',(context))
# def detail(request, photo_id):

#     photo = get_object_or_404(Photo, pk=photo_id)
#     return render(request, 'gallery/detail.html', {'photo': photo})
# def results(request, photo_id):


#     photo = get_object_or_404(Photo, pk=photo_id)
#     return render(request, 'gallery/results.html', {'photo': photo})
