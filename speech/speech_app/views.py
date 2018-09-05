import os
import json
import requests

from django.shortcuts import render
from django.http import HttpResponse

from watson_developer_cloud import AuthorizationV1 as Authorization
from watson_developer_cloud import SpeechToTextV1 as SpeechToText


def index(request):
    return render(request, 'index.html')


def stream_view(request):
    return render(request, 'stream.html')


def non_stream_view(request):
    """
    View to interpret `speech-to-text`
    :param: request
    :return: render transcript text in client
    """

    if request.method == 'GET':
        return render(request, 'non-stream.html')
    else:
        speech_file = request.FILES['audio_file']  # gets the audio file from file uploader

        headers = {'Content-Type': '{}'.format(speech_file.content_type)}

        username = os.environ.get('username')
        password = os.environ.get('password')

        url = 'https://stream.watsonplatform.net/speech-to-text/api/v1/recognize'

        # sends post request to ibm watson speech to text api
        response_data = requests.post(url, data=speech_file,
                                      auth=(username, password),
                                      headers=headers)

        result = json.loads(response_data.content)

        transcript = ''
        message = True

        for text in result['results']:
            transcript += text["alternatives"][0]["transcript"]

        return render(request, 'non-stream.html', {'transcript': transcript, 'message':message})


def get_token(request):
    username = os.environ.get('username')
    password = os.environ.get('password')

    authorization = Authorization(username=username, password=password)

    return HttpResponse(authorization.get_token(url=SpeechToText.default_url),
                        content_type='text/plain')
