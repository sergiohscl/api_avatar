import requests
from django.shortcuts import render


def get_avatar(request):
    response = requests.get(
        'https://last-airbender-api.fly.dev/api/v1/characters'
    )
    avatares = response.json()
    print(avatares[0]['photoUrl'])
    return render(
        request, 'avatar.html', {'avatares': avatares}
    )
