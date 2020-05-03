from django.shortcuts import render, HttpResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

import requests
import json

from .models import *
# Create your views here.

base_url = 'https://telegg.ru/orig/bot'
chat_id = '415924423'
text = 'Ваш статус заказа изменен!'


@csrf_exempt
def notice_status(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode())
        status = data['status']
        if status == 'on-hold':
            message_text = Message.objects.get(title='on-hold').text
            response = requests.get(
                base_url + settings.TOKEN + '/sendMessage?chat_id=' + str(chat_id) + '&text=' + message_text)
        return HttpResponse('OK')
