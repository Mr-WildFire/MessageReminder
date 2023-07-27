from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
import datetime
from email_alert.models import Message, MESSAGE_LEVEL
from django.contrib.auth.decorators import login_required

import logging
logger = logging.getLogger(__name__)


# Create your views here.
def index(request):
    return HttpResponse("Hello World!")


@login_required
def add_message(request):
    """添加信息"""
    if request.method == "POST":
        body = request.body
        info = json.loads(body.decode())
        user_id = request.user.pk
        message = info.get("message")
        level = info.get("level")
        level = MESSAGE_LEVEL.get(level, 0)

        Message.objects.create(message_info=message,
                               message_level=level,
                               user_id=user_id)

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


@login_required
def get_message(request):
    "获取当天的待提示信息展示在主页面上"
    date_begin = datetime.datetime.now().date()
    date_end = (date_begin + datetime.timedelta(1))
    user_id = request.user.pk

    messages = Message.objects.filter(
        setup_time__range=[date_begin, date_end], user_id=user_id).order_by("-message_level")

    message_info = []
    for mess in messages:
        message_info.append(mess.message_info)
    message_info = ';'.join(message_info)

    return JsonResponse({"code": 200, "data": message_info})
