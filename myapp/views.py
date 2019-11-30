from django.shortcuts import render
from django.http import HttpResponse
from .models import Bb
from django.template import loader
from django.shortcuts import render


def index(request):
    bbs = Bb.objects.all()
    return render(request, 'myapp/index.html', {'bbs': bbs})
#    s = 'Список объявлений\r\n\r\n\r\n'
#    for bb in Bb.objects.order_by('-published'):
#        s += bb.title  + '\r\n' + bb.content + '\r\n\r\n'
#    return HttpResponse(s, content_type='text/plain; charset= utf-8')
# Create your views here.
