from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include('speech_app.urls', namespace='speechapp')),

]
