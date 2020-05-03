from django.shortcuts import render, HttpResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

import requests
import json

from .models import *
# Create your views here.

base_url = 'https://api.telegram.org/bot'
chat_id = '415924423'
text = 'Ваш статус заказа изменен!'


@csrf_exempt
def notice_status(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode())
        status = data['status']
        id_order = data['id']
        user_obj = User.objects.get(orders__contains=id_order)
        print(user_obj.chat_id)
        if status == 'on-hold':
            items = data['line_items']
            items_formated = ''
            for item in items:
                items_formated += item['name']
            message_text = Message.objects.get(title='on-hold').text.format(items=items_formated)
            response = requests.get(
                base_url + settings.TOKEN + '/sendMessage?chat_id=' + str(user_obj.chat_id) + '&text=' + message_text)
        return HttpResponse('OK')
