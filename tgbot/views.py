from django.shortcuts import render, HttpResponse
from django.conf import settings

import requests

# Create your views here.

base_url = 'https://telegg.ru/orig/bot'
chat_id = '415924423'
text = 'Ваш статус заказа изменен!'


def notice_status(request):
    if request.method == 'POST':
        response = requests.get(base_url + settings.TOKEN + '/sendMessage?chat_id=' + str(chat_id) + '&text=' + text)
        print(response.text)
        return HttpResponse('OK')