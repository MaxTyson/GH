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
    photo = get_object_or_404(Photo, pk=photo_id)
    try:
        selected_like = photo.like_set.get(pk=request.POST['like'])
    except (KeyError, Like.DoesNotExist):
        # Redisplay the question add like form.
        return render(request, 'gallery/detail.html', {
            'photo': photo,
            'error_message': "You didn't add a like.",
        })
    else:
        selected_like.likes += 1
        selected_like.save()

        return HttpResponseRedirect(reverse('gallery:results', args=(photo_id,)))
