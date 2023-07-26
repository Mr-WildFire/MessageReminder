from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import json

import logging
logger = logging.getLogger(__name__)


# Create your views here.

def sign_up(request):
    """注册"""
    if request.method == "POST":
        body = request.body
        info = json.loads(body.decode())

        # 前端判断
        username = info.get("username")
        password = info.get("password")

        if User.objects.filter(username=username):
            result = {
                "code": 200,
                "message": "该用户名已经注册!"
            }
            response = JsonResponse(result, json_dumps_params={
                                    'ensure_ascii': False})  # 中文
            response.status_code = 200
            return response

        User.objects.create_user(username=username, password=password)
        result = {
            "code": 200,
            "message": "注册成功!"
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


def sign_in(request):
    """登录"""
    if request.method == "POST":
        body = request.body
        info = json.loads(body.decode())

        # 前端判断
        username = info.get("username")
        password = info.get("password")

        user = authenticate(username=username, password=password)
        login(request, user)

        logger.info(f"{username} 登录成功!")

        result = {
            "code": 200,
            "message": "登录成功!"
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


def sign_out(request):
    
    logout(request)
    result = {
        "code": 200,
        "message": "登出成功!"
    }
    response = JsonResponse(result, json_dumps_params={
        'ensure_ascii': False})  # 中文
    response.status_code = 200
    return response
