import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse

from .models import *


def Login(request):
    if request.method == 'GET':
        return render(request, 'identity/login.html')
    elif request.method == 'POST':
        un = request.POST.get('un')
        pw = request.POST.get('pw')

        users = User.objects.filter(username=un, password=pw)
        if users.exists():
            user = users.first()

            response = redirect(reverse('chat:home'))
            # 设置cookie
            # response.set_cookie('userid', user.id, expires=datetime.datetime.now() + datetime.timedelta(days=7))

            # 设置session
            request.session['userid'] = user.id
            request.session.set_expiry(7 * 24 * 3600)

            return response
        return HttpResponse('该用户不存在请注册！')


def Register(request):
    if request.method == 'GET':
        return render(request, 'identity/register.html')
    elif request.method == 'POST':
        un = request.POST.get('un')
        pw1 = request.POST.get('pw1')
        pw2 = request.POST.get('pw2')

        if pw1 != pw2:
            return HttpResponse('密码不匹配！')
        try:
            user = User()
            user.username = un
            user.password = pw1
            user.save()
        except Exception as e:
            return HttpResponse('注册失败！')
        return redirect(reverse('identity:login'))


def Logout(request):
    response = redirect(reverse('chat:home'))

    # 删除cookie
    # response.delete_cookie('userid')

    # 删除session
    session_key = request.session.session_key
    request.session.delete(session_key)

    return response
