from django.conf.urls import url
from .views import non_stream_view, get_token, index, stream_view


urlpatterns = [
    url(r'^$', index, name='speech'),
    url(r'^non-stream$', non_stream_view, name='non-streaming'),
    url(r'^stream', stream_view, name='non-streaming'),
    url(r'^api/speech-to-text/token$', get_token, name='watson-token'),

]