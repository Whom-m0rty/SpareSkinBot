from django.shortcuts import render, HttpResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

import requests

# Create your views here.

base_url = 'https://telegg.ru/orig/bot'
chat_id = '415924423'
text = 'Ваш статус заказа изменен!'


@csrf_exempt
def notice_status(request):
    if request.method == 'POST':
        response = requests.get(base_url + settings.TOKEN + '/sendMessage?chat_id=' + str(chat_id) + '&text=' + text)
        print(response.text)
        print(request.POST['status'])
        return HttpResponse('OK')
