from django.shortcuts import render

from identity.models import *


def home(request):
    # cookie
    # userid = request.COOKIES.get('userid', 0)

    # session
    userid = request.session.get('userid', 0)

    user = User.objects.filter(id=userid).first()
    return render(request, 'chat/home.html', {'user': user})


def room(request, room):
    return render(request, 'chat/room.html', {'room': room})
