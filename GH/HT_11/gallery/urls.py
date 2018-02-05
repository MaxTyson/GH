from django.conf.urls import url
from . import views

app_name = 'gallery'
urlpatterns = [
    # url(r'^$', views.index, name='index'),
    # url(r'^specifics/(?P<photo_id>[0-9]+)/$', views.detail, name='detail'),
    # url(r'^(P<photo_id>[0-9]+)/likes/$', views.add_like, name='likes by photo'),

    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<photo_id>[0-9]+)/add_like/$', views.add_like, name='add_like'),
]
