from django.conf.urls import url
from .views import speech_view


urlpatterns = [
    url(r'^$', speech_view, name='speech'),

]