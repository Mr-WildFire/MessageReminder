from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
import datetime
import pytz

from email_alert.models import Message


# Create your views here.


def index(request):
    return HttpResponse("Hello World!")


def add_message(request):
    if request.method == "POST":
        body = request.body
        info = json.loads(body.decode())

        message = info.get("message")
        Message.objects.create(message_info=message)

        result = {
            "code": 200,
            "message": "添加成功!",
        }
        response = JsonResponse(result, json_dumps_params={
                                'ensure_ascii': False})  # 中文
        response.status_code = 200
        return response
    else:
        result = {
            "code": 401,
            "message": "Method Not Allowed",
        }
        response = JsonResponse(result)
        response.status_code = 401
        return response


def get_message(request):

    date_begin = datetime.datetime.now().date()
    date_end = (date_begin + datetime.timedelta(1))
    # utc_timezone = pytz.timezone('UTC')
    # date_begin = utc_timezone.localize(date_begin)
    # date_end = utc_timezone.localize(date_end)

    messages = Message.objects.filter(setup_time__range=[date_begin, date_end])
    for mess in messages:
        print(mess.setup_time)
    return JsonResponse({"code": 200})
