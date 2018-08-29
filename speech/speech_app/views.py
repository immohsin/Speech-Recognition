import os
import json
import requests

from django.shortcuts import render


def speech_view(request):
    """
    View to interpret `speech-to-text`
    :param: request
    :return: render transcript text in client
    """

    if request.method == 'GET':
        return render(request, 'index.html')
    else:

        speech_file = request.FILES['audio_file']  # gets the audio file from file uploader

        headers = {'Content-Type': '{}'.format(speech_file.content_type)}

        username = os.environ.get('username')
        password = os.environ.get('password')

        url = os.environ.get('url')

        # sends post request to ibm watson speech to text api
        response_data = requests.post(url, data=speech_file,
                                      auth=(username, password),
                                      headers=headers)

        result = json.loads(response_data.content)

        transcript = ''
        message = True

        for text in result['results']:
            transcript += text["alternatives"][0]["transcript"]

        return render(request, 'index.html', {'transcript': transcript, 'message':message})
